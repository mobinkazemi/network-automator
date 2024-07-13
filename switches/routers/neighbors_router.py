from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from shared.dto.response.api_responseDto import SuccessResponseDto
from switches.dto.request.add_neighbor import AddNeighborSwitchDto
from .. import model
from db.database import session

router = APIRouter()


@router.post("/create/", response_model=SuccessResponseDto)
def create(data: AddNeighborSwitchDto):
    firstSwitch = (
        session.query(model.Switch).filter(model.Switch.id == data.from_id).first()
    )

    if firstSwitch is None:
        raise HTTPException(
            404, detail="سوییچ با آیدی {} پیدا نشد".format(data.from_id)
        )

    secondSwitch = (
        session.query(model.Switch).filter(model.Switch.id == data.to_id).first()
    )

    if secondSwitch is None:
        raise HTTPException(404, detail="سوییچ با آیدی {} پیدا نشد".format(data.to_id))

    firstSwitch.cdp.append(secondSwitch)
    secondSwitch.cdp.append(firstSwitch)

    session.commit()
    return {}


@router.delete("/delete/", response_model=SuccessResponseDto)
def delete(data: AddNeighborSwitchDto):
    print(data)
    firstSwitch = (
        session.query(model.Switch).filter(model.Switch.id == data.from_id).first()
    )

    if firstSwitch is None:
        raise HTTPException(
            404, detail="سوییچ با آیدی {} پیدا نشد".format(data.from_id)
        )

    secondSwitch = (
        session.query(model.Switch).filter(model.Switch.id == data.to_id).first()
    )

    if secondSwitch is None:
        raise HTTPException(404, detail="سوییچ با آیدی {} پیدا نشد".format(data.to_id))

    firstSwitch.cdp.remove(secondSwitch)
    secondSwitch.cdp.remove(firstSwitch)

    session.commit()
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
