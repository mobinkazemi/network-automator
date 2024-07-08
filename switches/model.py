from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base

switches_cdp = Table('switches_cdp', Base.metadata,
                     Column('id', Integer, primary_key=True, index=True),
                     Column('from_switch_id', Integer,
                            ForeignKey('switches.id')),
                     Column('to_switch_id', Integer, ForeignKey('switches.id'))
                     )


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
    cdp = relationship('Switch', secondary=switches_cdp,
                       primaryjoin=id == switches_cdp.c.from_switch_id,
                       secondaryjoin=id == switches_cdp.c.to_switch_id,
                       backref='connected_from')

    def __repr__(self):
        return f"<Switch(id={self.id}, name={self.name}, ip_address={self.ip_address})>"
