from dataclasses import dataclass
from pydantic import BaseModel

@dataclass(frozen=True)
class checkHardeningDto(BaseModel):
    id:int
    