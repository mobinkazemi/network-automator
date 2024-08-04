from shared.functions.to_dict import to_dict
from shared.repository.baseDeviceRepository import BaseNetworkDeviceRepository
from shared.repository.baseRepository import BaseRepository
from . import model
from sqlalchemy import delete as sql_delete
from switches.model import switches_cdp


class SwitchRepository(BaseNetworkDeviceRepository):
    def __init__(self) -> None:
        super().__init__(model.Switch)

    def deleteMeFromCDP(self, id: int):
        self.session.execute(
            sql_delete(switches_cdp).where(
                (switches_cdp.c.from_switch_id == id)
                | (switches_cdp.c.to_switch_id == id)
            )
        )

    def addCDP(self, first_id: int, second_id: int):
        firstSwitch = self.findOneRaw(first_id)
        secondSwitch = self.findOneRaw(second_id)

        firstSwitch.cdp.append(secondSwitch)
        secondSwitch.cdp.append(firstSwitch)

        self.session.commit()

    def deleteCDP(self, first_id: int, second_id: int):
        firstSwitch = self.findOneRaw(first_id)
        secondSwitch = self.findOneRaw(second_id)

        firstSwitch.cdp.remove(secondSwitch)
        secondSwitch.cdp.remove(firstSwitch)

        self.session.commit()
