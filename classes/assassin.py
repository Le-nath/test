
from .base import CharacterClass


class Assassin(CharacterClass):
    def __init__(self):
        super().__init__("Assassin", 10, 15, 5, "Attaque critique")
    
    def use_special(self, character, target):
        if self.special_cooldown > 0:
            print("Capacité spéciale en recharge!")
            return False
        
        import random
        critical_damage = character.attack * 2 + random.randint(5, 15)
        actual_damage = max(1, critical_damage - target.defense)
        target.hp -= actual_damage
        print(f"💥 {character.name} utilise Attaque critique et inflige {actual_damage} dégâts!")
        self.special_cooldown = 3
        return True
