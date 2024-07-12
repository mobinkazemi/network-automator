from pydantic import BaseModel
from dataclasses import dataclass


@dataclass(frozen=True)
class DeleteSwitchDto(BaseModel):
    id: int
