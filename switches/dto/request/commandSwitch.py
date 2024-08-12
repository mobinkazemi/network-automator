from dataclasses import dataclass
from pydantic import BaseModel


@dataclass(frozen=True)
class CommandSwitchDto(BaseModel):
    data: str
 
