
from .base import CharacterClass


class Archer(CharacterClass):
    def __init__(self):
        super().__init__("Archer", 15, 12, 7, "Tir perçant")
    
    def use_special(self, character, target):
        if self.special_cooldown > 0:
            print("Capacité spéciale en recharge!")
            return False
        
        import random
        piercing_damage = character.attack + 15 + random.randint(5, 12)
        # Tir perçant ignore 50% de la défense
        actual_damage = max(1, piercing_damage - (target.defense // 2))
        target.hp -= actual_damage
        print(f"🏹 {character.name} utilise Tir perçant et inflige {actual_damage} dégâts!")
        self.special_cooldown = 2
        return True
