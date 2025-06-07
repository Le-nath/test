
class CharacterClass:
    def __init__(self, name, hp_bonus, attack_bonus, defense_bonus, special_ability):
        self.name = name
        self.hp_bonus = hp_bonus
        self.attack_bonus = attack_bonus
        self.defense_bonus = defense_bonus
        self.special_ability = special_ability
        self.special_cooldown = 0
