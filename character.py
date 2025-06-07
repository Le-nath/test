import random


class Character:
  def __init__(self, name):
      self.name = name
      self.level = 1
      self.hp = 100
      self.max_hp = 100
      self.attack = 20
      self.defense = 10
      self.experience = 0
      self.gold = 50

  def display_stats(self):
      print(f"\n=== {self.name} ===")
      print(f"Niveau: {self.level}")
      print(f"PV: {self.hp}/{self.max_hp}")
      print(f"Attaque: {self.attack}")
      print(f"Défense: {self.defense}")
      print(f"Expérience: {self.experience}")
      print(f"Or: {self.gold}")

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

  def level_up(self):
      self.level += 1
      self.max_hp += 20
      self.hp = self.max_hp
      self.attack += 5
      self.defense += 3
      print(f"\n🎉 {self.name} monte au niveau {self.level}!")
      print(f"PV max: +20, Attaque: +5, Défense: +3")