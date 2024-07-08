from fastapi import APIRouter
from switches.router import router as switches_router

routes = APIRouter()

routes.include_router(switches_router, prefix="/switches", tags=["switches"])
