from shared.functions.to_dict import to_dict
from shared.repository.baseDeviceRepository import BaseNetworkDeviceRepository
from shared.repository.baseRepository import BaseRepository
from . import model


class SwitchRepository(BaseNetworkDeviceRepository):
    def __init__(self) -> None:
        super().__init__(model.Switch)
