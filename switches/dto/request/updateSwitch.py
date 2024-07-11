from pydantic import BaseModel
from dataclasses import dataclass


@dataclass(frozen=True)
class UpdateSwitchDto(BaseModel):
    id: int
    name: str | None = None
    ip: str | None = None
    username: str | None = None
    password: str | None = None
    portCount: int | None = None
    model: str | None = None
    series: str | None = None
    os: str | None = None
