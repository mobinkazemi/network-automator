from fastapi import APIRouter
from switches.routers.switches_router import router as switches_router
from switches.routers.neighbors_router import router as neighbors_router

routes = APIRouter()

routes.include_router(switches_router, prefix="/switches", tags=["switches"])
routes.include_router(neighbors_router, prefix="/switches/neighbor", tags=["switches"])
