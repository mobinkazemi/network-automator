from dataclasses import dataclass
from pydantic import BaseModel

@dataclass(frozen=True)
class CreateSwitchDto(BaseModel):
    name: str
    ip: str
    username: str | None = None
    password: str | None = None
    portCount: int | None = None
    model: str | None = None
    series: str | None = None
    os: str | None = None
