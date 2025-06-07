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