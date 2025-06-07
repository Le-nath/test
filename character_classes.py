
class CharacterClass:
    def __init__(self, name, hp_bonus, attack_bonus, defense_bonus, special_ability):
        self.name = name
        self.hp_bonus = hp_bonus
        self.attack_bonus = attack_bonus
        self.defense_bonus = defense_bonus
        self.special_ability = special_ability
        self.special_cooldown = 0

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
