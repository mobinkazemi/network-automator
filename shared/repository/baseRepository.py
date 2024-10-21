from sqlalchemy import select
from sqlalchemy.orm import Session
from db.database import session
from shared.functions.to_dict import to_dict


class BaseRepository:
    def __init__(self, model) -> None:
        self.model = model
        self.session: Session = session

    def createOne(self, data: dict) -> dict:
        instance = self.model(data)
        self.session.add(instance)
        self.session.commit()
        self.session.refresh(instance)
        return to_dict(instance)

    def findById(self, id: int):
        result = self.session.query(self.model).filter(self.model.id == id).first()

        if result is None:
            return None

        return to_dict(result)

    def findOne(self, **kwargs):
        return self.session.query(self.model).filter_by(**kwargs).first()

    def findOneRaw(self, id: int):
        result = self.session.query(self.model).filter(self.model.id == id).first()

        if result is None:
            return None

        return result

    def updateOne(self, id: int, updateData: dict):
        dbData = self.findById(id)

        self.session.query(self.model).filter(self.model.id == id).update(
            {**dbData, **updateData}
        )

        self.session.commit()

        return self.findById(id)

    def deleteOne(self, id: int):
        self.session.query(self.model).filter(self.model.id == id).delete()
        session.commit()

    def findAll(self):
        query = select(self.model).order_by(self.model.id)
        rawResult = self.session.execute(query)

        records = rawResult.scalars().all()

        result = [record.__dict__ for record in records]

        # remove internal state from the dict
        for item in result:
            item.pop("_sa_instance_state", None)

        return result
        return []
