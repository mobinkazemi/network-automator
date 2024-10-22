from sqlalchemy import Column, Integer, String
from db.database import Base, engine


class Hardening(Base):
    __tablename__ = "hardening"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    audit = Column(String, nullable=True)
    command = Column(String, nullable=False)
    recommendations = Column(String, nullable=True)
    regexPattern = Column(String ,nullable=True)
    # status = Column(bool, nullable=True)
    def __init__(self, data: any):
        try:
            self.title = data.title
            self.description = data.description
            self.audit = data.audit
            self.command = data.command
            self.recommendations = data.recommendations
            self.regexPattern = data.regexPattern

        except Exception as e:
            print(e)
            
        try:
            self.title = data["title"]
            self.description = data["description"]
            self.audit = data["audit"]
            self.command = data["command"]
            self.recommendations = data["recommendations"]
            self.regexPattern = data["regexPattern"]
        except Exception as e:
            print()


Base.metadata.create_all(engine)
