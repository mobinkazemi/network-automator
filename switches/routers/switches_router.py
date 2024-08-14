from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy import delete as sql_delete
from shared.dto.response.api_responseDto import SuccessResponseDto
from shared.functions.sanitize_request_dto import sanitizeRequestData
from switches.dto.request.commandSwitch import CommandSwitchDto
from switches.dto.request.deleteSwitch import DeleteSwitchDto
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


@router.post("/execCommand/", response_model=SuccessResponseDto)
def execCommand(data: CommandSwitchDto):

    # ssh.close()

    try:
        client = paramiko.Transport(("192.168.1.5", 22))
        client.connect(username="admin", password="admin")
        ssh = paramiko.SSHClient()
        ssh._transport = client
        stdin, stdout, stderr = ssh.exec_command(data.data)
        output = stdout.read().decode()
        client.close()
        return {"message": output, output: "اتصال  موفق"}

    except Exception as e:
        outputFile = open(f"ERR.txt", "a+")
        outputFile.write("\n***********" + "*****************\n")
        outputFile.write(str(e))
        outputFile.close()
        return {"message": "اتصال نا موفق"}


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


@router.post("/create/", response_model=SuccessResponseDto)
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
