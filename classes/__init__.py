
from .assassin import Assassin
from .guerrier import Guerrier
from .mage import Mage
from .archer import Archer
from .soutien import Soutien
from .base import CharacterClass

def get_available_classes():
    return {
        "1": Assassin(),
        "2": Guerrier(),
        "3": Mage(),
        "4": Archer(),
        "5": Soutien()
    }

def display_classes():
    print("\n=== Classes disponibles ===")
    print("1. Assassin - Attaque élevée, faible défense, attaque critique)")
    print("2. Guerrier - PV élevés, défense élevée, charge puissante")
    print("3. Mage - Attaque magique élevée, boule de feu")
    print("4. Archer - Équilibré, tir perçant")
    print("5. Soutien - Défense correcte, soin majeur")
