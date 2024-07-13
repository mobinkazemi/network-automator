from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy import delete as sql_delete
from shared.dto.response.api_responseDto import SuccessResponseDto
from switches.dto.request.deleteSwitch import DeleteSwitchDto
from .. import model
from pydantic import BaseModel
from switches.dto.request.createSwitch import CreateSwitchDto
from switches.dto.request.updateSwitch import UpdateSwitchDto
from shared.functions.to_dict import to_dict
from shared.functions.validate_ip import isValidIP
from switches.routers.neighbors_router import delete as delete_neighbors
from switches.model import switches_cdp
from db.database import session

router = APIRouter()


@router.post("/execCommand/", response_model=SuccessResponseDto)
def execCommand(command: str):
    return {"message": "درخواست اجرا شد", "data": command}


@router.post("/create/", response_model=SuccessResponseDto)
def create(data: CreateSwitchDto):
    if isValidIP(data.ip) is not True:
        raise HTTPException(400, detail="آی‌پی سوییج معتبر نیست")

    existing_switch = (
        session.query(model.Switch).filter(model.Switch.ip == data.ip).first()
    )
    if existing_switch:
        raise HTTPException(409, detail="آی‌پی سوییج تکراری است")
    switch = model.Switch(data)
    session.add(switch)
    session.commit()
    session.refresh(switch)
    return {"message": "درخواست انجام شد", "data": to_dict(switch)}


@router.patch("/update/", response_model=SuccessResponseDto)
def update(data: UpdateSwitchDto):
    thisSwitch = session.query(model.Switch).filter(model.Switch.id == data.id).first()

    if thisSwitch is None:
        raise HTTPException(404, detail="سوییج پیدا نشد")

    if data.ip and isValidIP(data.ip) is not True:
        raise HTTPException(400, detail="آی‌پی سوییج معتبر نیست")

    if (
        data.ip
        and session.query(model.Switch)
        .filter(model.Switch.ip == data.ip, model.Switch.id != data.id)
        .first()
    ):
        raise HTTPException(409, detail="این آی‌پی قبلا برای سوییج دیگری تعریف شده است")

    dictData = data.model_dump()

    dictData = {k: v for k, v in dictData.items() if v is not None}

    session.query(model.Switch).filter(model.Switch.id == data.id).update(
        {
            **to_dict(thisSwitch),
            **dictData,
        }
    )

    session.commit()

    return {
        "message": "درخواست انجام شد",
        "data": {
            **to_dict(thisSwitch),
            **dictData,
        },
    }


@router.delete("/delete/", response_model=SuccessResponseDto)
def delete(data: DeleteSwitchDto):
    thisSwitch = session.query(model.Switch).filter(model.Switch.id == data.id).first()

    if thisSwitch is None:
        raise HTTPException(404, detail="سوییج پیدا نشد")

    session.execute(
        sql_delete(switches_cdp).where(
            (switches_cdp.c.from_switch_id == data.id)
            | (switches_cdp.c.to_switch_id == data.id)
        )
    )

    session.query(model.Switch).filter(model.Switch.id == data.id).delete()

    session.commit()

    return {}
