
from .base import CharacterClass


class Guerrier(CharacterClass):
    def __init__(self):
        super().__init__("Guerrier", 30, 10, 15, "Charge puissante")
    
    def use_special(self, character, target):
        if self.special_cooldown > 0:
            print("Capacité spéciale en recharge!")
            return False
        
        import random
        charge_damage = character.attack + 20 + random.randint(0, 10)
        actual_damage = max(1, charge_damage - target.defense)
        target.hp -= actual_damage
        print(f"⚔️ {character.name} utilise Charge puissante et inflige {actual_damage} dégâts!")
        self.special_cooldown = 4
        return True
