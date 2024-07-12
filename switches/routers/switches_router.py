from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from db.database import get_db
from shared.dto.response.api_responseDto import  SuccessResponseDto
from switches.dto.request.deleteSwitch import DeleteSwitchDto
from .. import model
from pydantic import BaseModel
from switches.dto.request.createSwitch import CreateSwitchDto
from switches.dto.request.updateSwitch import UpdateSwitchDto
from shared.functions.to_dict import to_dict
from shared.functions.validate_ip import isValidIP

router = APIRouter()

@router.post('/execCommand/', response_model=SuccessResponseDto)
def execCommand(command: str):
    return {"message": "درخواست اجرا شد", "data": command}

@router.post('/create/',response_model=SuccessResponseDto)
def create(data: CreateSwitchDto, db: Session = Depends(get_db)):
    if isValidIP(data.ip) is not True:
        raise HTTPException(400, detail='آی‌پی سوییج معتبر نیست')

    existing_switch = db.query(model.Switch).filter(
        model.Switch.ip == data.ip).first()
    if existing_switch:
        raise HTTPException(409, detail='آی‌پی سوییج تکراری است')
    switch = model.Switch(data)
    db.add(switch)
    db.commit()
    db.refresh(switch)
    return {
        "message": "درخواست انجام شد",
        "data": to_dict(switch)
    }

@router.patch('/update/',response_model=SuccessResponseDto)
def update(data: UpdateSwitchDto, db: Session = Depends(get_db)):
    thisSwitch = db.query(model.Switch).filter(
        model.Switch.id == data.id).first()

    if thisSwitch is None:
        raise HTTPException(404, detail='سوییج پیدا نشد')

    if data.ip and isValidIP(data.ip) is not True:
        raise HTTPException(400, detail='آی‌پی سوییج معتبر نیست')
    
    if data.ip and db.query(model.Switch).filter(model.Switch.ip == data.ip, model.Switch.id != data.id).first():
        raise HTTPException(
            409, detail="این آی‌پی قبلا برای سوییج دیگری تعریف شده است")

    dictData = data.model_dump()

    dictData = {k: v for k, v in dictData.items() if v is not None}

    db.query(model.Switch).filter(
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

@router.delete('/delete/', response_model=SuccessResponseDto)
def delete(data: DeleteSwitchDto, db: Session = Depends(get_db)):
    thisSwitch = db.query(model.Switch).filter(
        model.Switch.id == data.id).first()

    if thisSwitch is None:
        raise HTTPException(404, detail='سوییج پیدا نشد')

    db.query(model.Switch).filter(
        model.Switch.id == data.id).delete()
    
    db.commit()

    return {}
