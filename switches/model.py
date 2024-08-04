from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base, engine
from switches.dto.request.createSwitch import CreateSwitchDto

switches_cdp = Table(
    "switches_cdp",
    Base.metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("from_switch_id", Integer, ForeignKey("switches.id")),
    Column("to_switch_id", Integer, ForeignKey("switches.id")),
)

# class Switch_CDP(Base):
#     __tablename__ = "switches_cdp"
#     id = Column(Integer, primary_key=True, index=True)
#     from_switch_id= Column( Integer, ForeignKey("switches.id")),
#     to_switch_id= Column( Integer, ForeignKey("switches.id")),


class Switch(Base):
    __tablename__ = "switches"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    ip = Column(String, unique=True, nullable=False)
    username = Column(String, nullable=True)
    password = Column(String, nullable=True)
    portCount = Column(Integer, nullable=True)
    model = Column(String, nullable=True)
    series = Column(String, nullable=True)
    os = Column(String, nullable=True)
    cdp = relationship(
        "Switch",
        secondary=switches_cdp,
        primaryjoin=id == switches_cdp.c.from_switch_id,
        secondaryjoin=id == switches_cdp.c.to_switch_id,
        backref="connected_from",
    )

    def __init__(self, data: CreateSwitchDto):
        self.name = data.name
        self.ip = data.ip
        self.username = data.username
        self.password = data.password
        self.portCount = data.portCount
        self.model = data.model
        self.series = data.series
        self.os = data.os


Base.metadata.create_all(engine)
