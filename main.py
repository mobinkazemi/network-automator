from typing import Union
from fastapi import FastAPI
from router import routes as api_router
from db.database import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(api_router)