import random


class Character:
  def __init__(self, name, character_class=None):
      self.name = name
      self.level = 1
      self.character_class = character_class
      
      # Stats de base
      base_hp = 100
      base_attack = 20
      base_defense = 10
      
      # Appliquer les bonus de classe
      if character_class:
          self.hp = base_hp + character_class.hp_bonus
          self.max_hp = self.hp
          self.attack = base_attack + character_class.attack_bonus
          self.defense = base_defense + character_class.defense_bonus
      else:
          self.hp = base_hp
          self.max_hp = base_hp
          self.attack = base_attack
          self.defense = base_defense
      
      self.experience = 0
      self.gold = 50

  def display_stats(self):
      print(f"\n=== {self.name} ===")
      if self.character_class:
          print(f"Classe: {self.character_class.name}")
      print(f"Niveau: {self.level}")
      print(f"PV: {self.hp}/{self.max_hp}")
      print(f"Attaque: {self.attack}")
      print(f"Défense: {self.defense}")
      print(f"Expérience: {self.experience}")
      print(f"Or: {self.gold}")
      if self.character_class and self.character_class.special_cooldown > 0:
          print(f"Capacité spéciale: {self.character_class.special_cooldown} tours restants")

  def attack_monster(self, monster):
      damage = max(1, self.attack - monster.defense + random.randint(-5, 5))
      monster.hp -= damage
      print(f"{self.name} attaque {monster.name} et inflige {damage} dégâts!")
      return damage

  def take_damage(self, damage):
      actual_damage = max(1, damage - self.defense)
      self.hp -= actual_damage
      print(f"{self.name} reçoit {actual_damage} dégâts!")
      return actual_damage

  def heal(self):
      if self.gold >= 20:
          heal_amount = random.randint(20, 40)
          self.hp = min(self.max_hp, self.hp + heal_amount)
          self.gold -= 20
          print(f"{self.name} se soigne et récupère {heal_amount} PV!")
      else:
          print("Pas assez d'or pour se soigner!")

  def use_special_ability(self, target=None):
      if not self.character_class:
          print("Aucune classe sélectionnée!")
          return False
      
      return self.character_class.use_special(self, target)
  
  def reduce_cooldowns(self):
      if self.character_class and self.character_class.special_cooldown > 0:
          self.character_class.special_cooldown -= 1

  def level_up(self):
      self.level += 1
      self.max_hp += 20
      self.hp = self.max_hp
      self.attack += 5
      self.defense += 3
      print(f"\n🎉 {self.name} monte au niveau {self.level}!")
      print(f"PV max: +20, Attaque: +5, Défense: +3")