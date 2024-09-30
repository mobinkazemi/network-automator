from sqlalchemy import Column, Integer, String
from db.database import Base, engine
from users.dto.request.createUser import CreateUserDto


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)

    def __init__(self, data: CreateUserDto):
        self.name = data.name
        self.username = data.username
        self.password = data.password


Base.metadata.create_all(engine)
