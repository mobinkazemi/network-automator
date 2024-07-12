from dataclasses import dataclass
from pydantic import BaseModel

@dataclass(frozen=True)
class DeleteNeighborSwitchDto(BaseModel):
    from_id:int
    to_id:int
