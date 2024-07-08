from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .dto.createSwitch import CreateSwitchDto
from db.database import get_db
from . import model

router = APIRouter()


@router.post('/execCommand')
def execCommand(command: str):
    return {"message": "درخواست اجرا شد", "data": command}


@router.post('/create/')
def create(data: CreateSwitchDto, db: Session = Depends(get_db)):
    switch = model.Switch(data)
    db.add(switch)
    db.commit()
    db.refresh(switch)
    return switch
