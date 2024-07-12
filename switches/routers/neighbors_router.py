from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from shared.dto.response.api_responseDto import  SuccessResponseDto
from switches.dto.request.add_neighbor import AddNeighborSwitchDto
from .. import model

router = APIRouter()

@router.post('/create/',response_model=SuccessResponseDto)
def create(data: AddNeighborSwitchDto, db: Session = Depends(get_db)):
    firstSwitch = db.query(model.Switch).filter(
        model.Switch.id == data.from_id
    ).first()

    if firstSwitch is None:
        raise HTTPException(404, detail='سوییچ با آیدی {} پیدا نشد'.format(data.from_id))

    secondSwitch = db.query(model.Switch).filter(
        model.Switch.id == data.to_id
    ).first()

    if secondSwitch is None:
        raise HTTPException(404, detail='سوییچ با آیدی {} پیدا نشد'.format(data.to_id))
    
    firstSwitch.cdp.append(secondSwitch)
    secondSwitch.cdp.append(firstSwitch)

    db.commit()
    return {}

@router.delete('/delete/',response_model=SuccessResponseDto)
def delete(data: AddNeighborSwitchDto, db: Session = Depends(get_db)):
    print(data)
    firstSwitch = db.query(model.Switch).filter(
        model.Switch.id == data.from_id
    ).first()

    if firstSwitch is None:
        raise HTTPException(404, detail='سوییچ با آیدی {} پیدا نشد'.format(data.from_id))

    secondSwitch = db.query(model.Switch).filter(
        model.Switch.id == data.to_id
    ).first()

    if secondSwitch is None:
        raise HTTPException(404, detail='سوییچ با آیدی {} پیدا نشد'.format(data.to_id))
    
    firstSwitch.cdp.remove(secondSwitch)
    secondSwitch.cdp.remove(firstSwitch)

    db.commit()
    return {}



# @router.delete('/delete/', response_model=SuccessResponseDto)
# def delete(data: DeleteSwitchDto, db: Session = Depends(get_db)):
#     thisSwitch = db.query(model.Switch).filter(
#         model.Switch.id == data.id).first()

#     if thisSwitch is None:
#         raise HTTPException(404, detail='سوییج پیدا نشد')

#     db.query(model.Switch).filter(
#         model.Switch.id == data.id).delete()
    
#     db.commit()

#     return {}
