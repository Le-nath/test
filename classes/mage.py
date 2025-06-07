
from .base import CharacterClass


class Mage(CharacterClass):
    def __init__(self):
        super().__init__("Mage", 0, 20, 8, "Boule de feu")
    
    def use_special(self, character, target):
        if self.special_cooldown > 0:
            print("Capacité spéciale en recharge!")
            return False
        
        import random
        magic_damage = 25 + random.randint(10, 20)
        target.hp -= magic_damage  # Dégâts magiques ignorent la défense
        print(f"🔥 {character.name} lance Boule de feu et inflige {magic_damage} dégâts magiques!")
        self.special_cooldown = 3
        return True
