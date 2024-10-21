from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from shared.dto.response.api_responseDto import SuccessResponseDto
from switches.dto.request.add_neighbor import AddNeighborSwitchDto
from switches.repository import SwitchRepository
from .. import model
from db.database import session

router = APIRouter()
switchRepo = SwitchRepository()


@router.post("/create/", response_model=SuccessResponseDto)
def create(data: AddNeighborSwitchDto):
    firstSwitch = switchRepo.findById(data.from_id)

    if firstSwitch is None:
        raise HTTPException(
            404, detail="سوییچ با آیدی {} پیدا نشد".format(data.from_id)
        )

    secondSwitch = switchRepo.findById(data.to_id)

    if secondSwitch is None:
        raise HTTPException(404, detail="سوییچ با آیدی {} پیدا نشد".format(data.to_id))

    switchRepo.addCDP(data.from_id, data.to_id)

    return {}


@router.delete("/delete/", response_model=SuccessResponseDto)
def delete(data: AddNeighborSwitchDto):
    firstSwitch = switchRepo.findById(data.from_id)

    if firstSwitch is None:
        raise HTTPException(
            404, detail="سوییچ با آیدی {} پیدا نشد".format(data.from_id)
        )

    secondSwitch = switchRepo.findById(data.to_id)

    if secondSwitch is None:
        raise HTTPException(404, detail="سوییچ با آیدی {} پیدا نشد".format(data.to_id))

    switchRepo.deleteCDP(data.from_id, data.to_id)

    return {}


# @router.delete('/delete/', response_model=SuccessResponseDto)
# def delete(data: DeleteSwitchDto):
#     thisSwitch =session.query(model.Switch).filter(
#         model.Switch.id == data.id).first()

#     if thisSwitch is None:
#         raise HTTPException(404, detail='سوییج پیدا نشد')

#    session.query(model.Switch).filter(
#         model.Switch.id == data.id).delete()

#    session.commit()

#     return {}
