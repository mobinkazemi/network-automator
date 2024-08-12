from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

url = URL.create(
    drivername="postgresql",
    username="maxsusi",
    password="2783@Rtda",
    host="localhost",
    database="maxsusi",
    port=5432,
)

engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
