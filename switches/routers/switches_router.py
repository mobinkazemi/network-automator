from fastapi import APIRouter, Depends, HTTPException, Request
from auth.functions.get_user_or_error import get_user_or_error
from shared.classes.Session_Manager import SessionManager
from shared.dto.response.api_responseDto import SuccessResponseDto
from shared.functions.get_client_id import getClientId
from shared.functions.sanitize_request_dto import sanitizeRequestData
from switches.dto.request.commandSwitch import CommandSwitchDto
from switches.functions.check_connection import check_ssh_connection
from switches.functions.check_connection import run_multiple_commands_separately
from switches.repository import SwitchRepository
from .. import model
from switches.dto.request.createSwitch import CreateSwitchDto
from switches.dto.request.updateSwitch import UpdateSwitchDto
from switches.dto.request.checkHardening import checkHardeningDto
from shared.functions.validate_ip import isValidIP
from db.database import session
import paramiko
import asyncio
import time

router = APIRouter()
switchRepo = SwitchRepository()
sessionManager = SessionManager()


@router.post("/execCommand", response_model=SuccessResponseDto)
def execCommand(
    req: Request, data: CommandSwitchDto, payload: dict = Depends(get_user_or_error)
):
    # if data.data == "A":
    #     raise HTTPException(412, detail="اتصال به سوییچ ناموفق بود")
    # else:
    #     return {"data": {"stdout": data.data, "stderr": 2}}

    thisSwitch = switchRepo.findById(data.switchId)
    if not thisSwitch:
        raise HTTPException(404, detail="سوییچ پیدا نشد")

    clientId = getClientId(req)
    if not clientId:
        raise HTTPException(412, detail="شناسه کلاینت دریافت نشد")

    sessionKey = sessionManager.getKey(
        clientId=clientId, deviceId=thisSwitch["id"], deviceType="switch"
    )

    if not sessionManager.hasClient(sessionKey):
        try:
            client = paramiko.Transport((thisSwitch["ip"], 22))
            client.connect(
                username=thisSwitch["username"], password=thisSwitch["password"]
            )
            ssh = paramiko.SSHClient()
            ssh._transport = client

        except Exception as e:
            raise HTTPException(412, detail="اتصال به سوییچ ناموفق بود")

        sessionManager.setClient(sessionKey, ssh)

    thisSession = sessionManager.getClient(sessionKey)
    stdin, stdout, stderr = thisSession.exec_command(data.data)
    resultOutput = stdout.read().decode()
    resultError = stderr.read().decode()
    return {
        "message": "درخواست انجام شد",
        "data": {"stdout": resultOutput, "stderr": resultError},
    }


@router.get("/checkConnectionStatus", response_model=SuccessResponseDto)
async def checkConnectionStatus(payload: dict = Depends(get_user_or_error)):
    tasks = []
    finalResult = []
    batch_size = 10  # number of tasks per batch
    ttl = 2  # seconds
    allSwitches = switchRepo.findAll()

    for sw in allSwitches:
        tasks.append(asyncio.create_task(check_ssh_connection(sw, ttl)))

    tasks = [tasks[i : i + batch_size] for i in range(0, len(tasks), batch_size)]
    for i in range(len(tasks)):
        thisResults = await asyncio.gather(*tasks[i])
        finalResult.extend(thisResults)

    return {"data": finalResult, "message": "درخواست انجام شد"}


@router.get("/info/{id}", response_model=SuccessResponseDto)
def info(
    id: int,
    payload: dict = Depends(get_user_or_error),
):
    thisSwitch = switchRepo.findById(id)

    if thisSwitch is None:
        raise HTTPException(404, detail="سوییچ پیدا نشد")

    return {"data": thisSwitch}


@router.get("/byIP/{ip}", response_model=SuccessResponseDto)
def byIP(ip: str, payload: dict = Depends(get_user_or_error)):
    thisSwitch = switchRepo.findByIP(ip)
    print("test")
    if thisSwitch is None:
        raise HTTPException(404, detail="سوییچ پیدا نشد")

    return {"data": thisSwitch}


@router.post("/create", response_model=SuccessResponseDto)
def create(data: CreateSwitchDto, payload: dict = Depends(get_user_or_error)):
    if isValidIP(data.ip) is not True:
        raise HTTPException(400, detail="آی‌پی سوییج معتبر نیست")

    existing_switch = (
        session.query(model.Switch).filter(model.Switch.ip == data.ip).first()
    )

    if existing_switch:
        raise HTTPException(409, detail="آی‌پی سوییج تکراری است")

    switch = switchRepo.createOne(data)

    return {"message": "درخواست انجام شد", "data": switch}


@router.patch("/update/", response_model=SuccessResponseDto)
def update(data: UpdateSwitchDto, payload: dict = Depends(get_user_or_error)):
    thisSwitch = switchRepo.findById(data.id)
    if thisSwitch is None:
        raise HTTPException(404, detail="سوییج پیدا نشد")

    if data.ip and isValidIP(data.ip) is not True:
        raise HTTPException(400, detail="آی‌پی سوییج معتبر نیست")

    switchWithThisIp = switchRepo.findByIP(data.ip)
    if data.ip and switchWithThisIp and switchWithThisIp["id"] != data.id:
        raise HTTPException(409, detail="این آی‌پی قبلا تعریف شده است")

    result = switchRepo.updateOne(data.id, sanitizeRequestData(data))

    return {"data": result}


@router.delete("/delete/{id}", response_model=SuccessResponseDto)
def delete(id: int, payload: dict = Depends(get_user_or_error)):
    thisSwitch = switchRepo.findById(id)

    if thisSwitch is None:
        raise HTTPException(404, detail="سوییج پیدا نشد")

    switchRepo.deleteMeFromCDP(id)

    switchRepo.deleteOne(id)

    return {}


@router.get("/list", response_model=SuccessResponseDto)
def findAll(req: Request, payload: dict = Depends(get_user_or_error)):
    switchesList = switchRepo.findAll()
    print(req.headers.get("clientId"))
    return {"data": switchesList}


@router.get("/checkHardening", response_model=SuccessResponseDto)
def checkHardening(
    req: Request, data: checkHardeningDto, payload: dict = Depends(get_user_or_error)
):
    thisSwitch = switchRepo.findById(data.id)
    if not thisSwitch:
        raise HTTPException(404, detail="سوییچ پیدا نشد")

    clientId = getClientId(req)
    if not clientId:
        raise HTTPException(412, detail="شناسه کلاینت دریافت نشد")

    sessionKey = sessionManager.getKey(
        clientId=clientId, deviceId=thisSwitch["id"], deviceType="switch"
    )

    if not sessionManager.hasClient(sessionKey):
        try:
            commandsOutput = run_multiple_commands_separately(
                thisSwitch["ip"],
                username=thisSwitch["username"],
                password=thisSwitch["password"],
            )
        except Exception as e:
            raise HTTPException(412, detail="اتصال به سوییچ ناموفق بود")

    # thisSession = sessionManager.getClient(sessionKey)

    time.sleep(5)

    # resultError = stderr.read().decode()

    return {
        "message": "درخواست انجام شد",
        "data": {"stdout": commandsOutput, "stderr": "resultError"},
    }
