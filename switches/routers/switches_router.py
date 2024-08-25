from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy import delete as sql_delete
from shared.dto.response.api_responseDto import SuccessResponseDto
from shared.functions.sanitize_request_dto import sanitizeRequestData
from switches.dto.request.commandSwitch import CommandSwitchDto
from switches.dto.request.deleteSwitch import DeleteSwitchDto
from switches.functions.check_connection import check_ssh_connection
from switches.repository import SwitchRepository
from .. import model
from pydantic import BaseModel
from switches.dto.request.createSwitch import CreateSwitchDto
from switches.dto.request.updateSwitch import UpdateSwitchDto
from shared.functions.to_dict import to_dict
from shared.functions.validate_ip import isValidIP
from switches.routers.neighbors_router import delete as delete_neighbors
from switches.model import switches_cdp
from db.database import session
import paramiko

router = APIRouter()
switchRepo = SwitchRepository()


@router.post("/execCommand", response_model=SuccessResponseDto)
def execCommand(data: CommandSwitchDto):
    # if data.data == "A":
    #     raise HTTPException(412, detail="اتصال به سوییچ ناموفق بود")
    # else:
    #     return {"data": {"stdout": data.data, "stderr": 2}}

    thisSwitch = switchRepo.findOne(data.switchId)

    if not thisSwitch:
        raise HTTPException(404, detail="سوییچ پیدا نشد")

    try:
        client = paramiko.Transport((thisSwitch["ip"], 22))
        client.connect(username=thisSwitch["username"], password=thisSwitch["password"])
        ssh = paramiko.SSHClient()
        ssh._transport = client
        stdin, stdout, stderr = ssh.exec_command(data.data)
        resultOutput = stdout.read().decode()
        resultError = stderr.read().decode()
        client.close()
        return {
            "message": "درخواست انجام شد",
            "data": {"stdout": resultOutput, "stderr": resultError},
        }

    except Exception as e:
        raise HTTPException(412, detail="اتصال به سوییچ ناموفق بود")


@router.get("/checkConnectionStatus", response_model=SuccessResponseDto)
def checkConnectionStatus():

    allSwitches = switchRepo.findAll()
    finalResult = []

    for sw in allSwitches:
        result = check_ssh_connection(sw)
        finalResult.append({"id": sw["id"], "result": result})

    return {"data": finalResult, "message": "درخواست انجام شد"}


@router.get("/info/{id}", response_model=SuccessResponseDto)
def info(id: int):
    thisSwitch = switchRepo.findOne(id)

    if thisSwitch is None:
        raise HTTPException(404, detail="سوییچ پیدا نشد")

    return {"data": thisSwitch}


@router.get("/byIP/{ip}", response_model=SuccessResponseDto)
def byIP(ip: str):
    thisSwitch = switchRepo.findByIP(ip)
    print("test")
    if thisSwitch is None:
        raise HTTPException(404, detail="سوییچ پیدا نشد")

    return {"data": thisSwitch}


@router.post("/create", response_model=SuccessResponseDto)
def create(data: CreateSwitchDto):
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
def update(data: UpdateSwitchDto):
    thisSwitch = switchRepo.findOne(data.id)
    if thisSwitch is None:
        raise HTTPException(404, detail="سوییج پیدا نشد")

    if data.ip and isValidIP(data.ip) is not True:
        raise HTTPException(400, detail="آی‌پی سوییج معتبر نیست")

    if data.ip and switchRepo.findByIP(data.ip):
        raise HTTPException(409, detail="این آی‌پی قبلا تعریف شده است")

    result = switchRepo.updateOne(data.id, sanitizeRequestData(data))

    return {"data": result}


@router.delete("/delete/{id}", response_model=SuccessResponseDto)
def delete(id: int):
    thisSwitch = switchRepo.findOne(id)

    if thisSwitch is None:
        raise HTTPException(404, detail="سوییج پیدا نشد")

    switchRepo.deleteMeFromCDP(id)

    switchRepo.deleteOne(id)

    return {}


@router.get("/list", response_model=SuccessResponseDto)
def findAll():
    switchesList = switchRepo.findAll()

    return {"data": switchesList}
