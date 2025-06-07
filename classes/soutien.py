
from .base import CharacterClass


class Soutien(CharacterClass):
    def __init__(self):
        super().__init__("Soutien", 20, 5, 12, "Soin majeur")
    
    def use_special(self, character, target=None):
        if self.special_cooldown > 0:
            print("Capacité spéciale en recharge!")
            return False
        
        import random
        heal_amount = random.randint(30, 50)
        character.hp = min(character.max_hp, character.hp + heal_amount)
        print(f"✨ {character.name} utilise Soin majeur et récupère {heal_amount} PV!")
        self.special_cooldown = 4
        return True
