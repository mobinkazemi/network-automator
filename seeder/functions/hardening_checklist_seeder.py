from hardening.repository import HardeningRepository
from hardening.hardeningCheckList import hardeningCheckList

hardeningRepo = HardeningRepository()


def hardening_checklist_seeder():
    try:
        for item in hardeningCheckList:
            if not hardeningRepo.findOne(title=item["title"]):
                hardeningRepo.createOne(item)
        print("Hardening Seeder Executed")

    except:
        print("FAILED: Hardening seeder")
