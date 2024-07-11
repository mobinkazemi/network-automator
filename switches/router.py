from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from . import model
from pydantic import BaseModel
from switches.dto.request.createSwitch import CreateSwitchDto
from switches.dto.request.updateSwitch import UpdateSwitchDto
from shared.functions.to_dict import to_dict

router = APIRouter()


@router.post('/execCommand/')
def execCommand(command: str):
    return {"message": "درخواست اجرا شد", "data": command}


@router.post('/create/')
def create(data: CreateSwitchDto, db: Session = Depends(get_db)):
    existing_switch = db.query(model.Switch).filter(
        model.Switch.ip == data.ip).first()
    if existing_switch:
        raise HTTPException(409, detail='آیپی سوییج تکراری است')
    switch = model.Switch(data)
    db.add(switch)
    db.commit()
    db.refresh(switch)
    return {
        "message": "درخواست انجام شد",
        "data": switch
    }


@router.patch('/update/')
def update(data: UpdateSwitchDto, db: Session = Depends(get_db)):
    thisSwitch = db.query(model.Switch).filter(
        model.Switch.id == data.id).first()

    if thisSwitch is None:
        raise HTTPException(404, detail='سوییج پیدا نشد')

    if data.ip and db.query(model.Switch).filter(model.Switch.ip == data.ip, model.Switch.id != data.id).first():
        raise HTTPException(
            409, detail="این آی‌پی قبلا برای سوییج دیگری تعریف شده است")

    dictData = data.dict()

    dictData = {k: v for k, v in dictData.items() if v is not None}

    updatedSwitch = db.query(model.Switch).filter(
        model.Switch.id == data.id).update({
            **to_dict(thisSwitch),
            **dictData,
        })

    db.commit()

    return {
        "message": "درخواست انجام شد",
        "data": {
            **to_dict(thisSwitch),
            **dictData,
        }
    }
