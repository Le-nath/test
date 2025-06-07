import random


class Monster:
  def __init__(self, name, hp, attack, defense, exp_reward, gold_reward):
      self.name = name
      self.hp = hp
      self.max_hp = hp
      self.attack = attack
      self.defense = defense
      self.exp_reward = exp_reward
      self.gold_reward = gold_reward

  def attack_player(self, player):
      damage = max(1, self.attack + random.randint(-3, 3))
      player.take_damage(damage)
      return damage


def create_dungeon_monster(difficulty, player_level):
    """Crée un monstre adapté aux donjons avec difficulté variable"""
    base_monsters = [
        ("Squelette Guerrier", 40, 18, 6, 30, 20),
        ("Golem de Pierre", 70, 22, 12, 45, 30),
        ("Spectre", 35, 25, 4, 35, 25),
        ("Minotaure", 90, 28, 10, 60, 40)
    ]
    
    boss_monsters = [
        ("Liche Ancienne", 150, 35, 18, 120, 100),
        ("Dragon des Profondeurs", 200, 40, 20, 150, 120),
        ("Démon Gardien", 180, 38, 15, 140, 110)
    ]
    
    if difficulty == 2:  # Boss
        monsters = boss_monsters
    else:
        monsters = base_monsters
    
    base_monster = random.choice(monsters)
    name, hp, attack, defense, exp, gold = base_monster
    
    # Ajuste selon le niveau du joueur et la difficulté
    level_mod = (player_level - 1) * difficulty
    hp += level_mod * 8
    attack += level_mod * 2
    defense += level_mod * 1
    exp += level_mod * 8
    gold += level_mod * 4
    
    return Monster(name, hp, attack, defense, exp, gold)