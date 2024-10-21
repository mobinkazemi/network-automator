from hardening.repository import HardeningRepository
from seeder.functions.hardening_checklist_seeder import hardening_checklist_seeder


def seeder():
    print("\n\n")
    print("seeder is running:")
    hardening_checklist_seeder()
    print("seeder finished.")
    print("\n\n")
