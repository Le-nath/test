
import random


class Room:
    def __init__(self, room_type, description, content=None):
        self.room_type = room_type
        self.description = description
        self.content = content
        self.visited = False


class Dungeon:
    def __init__(self, name, size=5):
        self.name = name
        self.size = size
        self.rooms = self.generate_rooms()
        self.current_room = 0
        self.completed = False
    
    def generate_rooms(self):
        rooms = []
        room_types = [
            ("empty", "Une salle vide avec des toiles d'araignées."),
            ("treasure", "Une salle qui scintille d'or et de gemmes."),
            ("monster", "Une salle sombre où rôde un monstre."),
            ("trap", "Une salle pleine de pièges dangereux."),
            ("healing", "Une source magique qui restaure la santé."),
            ("mysterious", "Une salle mystérieuse avec une aura étrange.")
        ]
        
        # Première salle toujours vide (entrée)
        rooms.append(Room("entrance", "L'entrée du donjon. Des torches éclairent faiblement les murs."))
        
        # Générer les salles du milieu
        for i in range(self.size - 2):
            room_type, description = random.choice(room_types)
            content = self.generate_room_content(room_type)
            rooms.append(Room(room_type, description, content))
        
        # Dernière salle avec boss ou trésor final
        boss_room = Room("boss", "La salle du boss! Une présence maléfique emplit l'air.", 
                        {"type": "boss_monster", "difficulty": 2})
        rooms.append(boss_room)
        
        return rooms
    
    def generate_room_content(self, room_type):
        if room_type == "treasure":
            treasures = [
                {"type": "gold", "amount": random.randint(50, 150)},
                {"type": "potion", "healing": random.randint(30, 60)},
                {"type": "equipment", "stat_boost": random.randint(2, 5)}
            ]
            return random.choice(treasures)
        
        elif room_type == "monster":
            return {"type": "dungeon_monster", "difficulty": 1}
        
        elif room_type == "trap":
            return {"type": "trap", "damage": random.randint(10, 25)}
        
        elif room_type == "healing":
            return {"type": "healing_fountain", "healing": random.randint(40, 80)}
        
        elif room_type == "mysterious":
            events = [
                {"type": "stat_boost", "stat": "attack", "amount": 3},
                {"type": "stat_boost", "stat": "defense", "amount": 2},
                {"type": "curse", "stat": "hp", "amount": -15},
                {"type": "experience", "amount": 50}
            ]
            return random.choice(events)
        
        return None
    
    def get_current_room(self):
        return self.rooms[self.current_room]
    
    def can_advance(self):
        return self.current_room < len(self.rooms) - 1
    
    def advance_room(self):
        if self.can_advance():
            self.current_room += 1
            return True
        return False
    
    def can_retreat(self):
        return self.current_room > 0
    
    def retreat_room(self):
        if self.can_retreat():
            self.current_room -= 1
            return True
        return False


def create_dungeon(player_level):
    dungeon_names = [
        "Crypte Oubliée",
        "Cavernes Sombres",
        "Ruines Anciennes",
        "Laboratoire du Mage Fou",
        "Forteresse Abandonnée"
    ]
    
    name = random.choice(dungeon_names)
    size = min(3 + player_level, 8)  # Taille augmente avec le niveau
    return Dungeon(name, size)


def explore_room(player, room):
    print(f"\n🏛️ {room.description}")
    
    if room.visited:
        print("Vous avez déjà exploré cette salle.")
        return
    
    room.visited = True
    
    if not room.content:
        print("La salle semble vide...")
        return
    
    content = room.content
    
    if content["type"] == "gold":
        player.gold += content["amount"]
        print(f"💰 Vous trouvez {content['amount']} pièces d'or!")
    
    elif content["type"] == "potion":
        healing = content["healing"]
        old_hp = player.hp
        player.hp = min(player.max_hp, player.hp + healing)
        actual_healing = player.hp - old_hp
        print(f"🧪 Vous trouvez une potion et récupérez {actual_healing} PV!")
    
    elif content["type"] == "equipment":
        boost = content["stat_boost"]
        stat_choice = random.choice(["attack", "defense"])
        if stat_choice == "attack":
            player.attack += boost
            print(f"⚔️ Vous trouvez une arme! Attaque +{boost}")
        else:
            player.defense += boost
            print(f"🛡️ Vous trouvez une armure! Défense +{boost}")
    
    elif content["type"] == "trap":
        damage = content["damage"]
        player.take_damage(damage)
        print(f"💥 Vous déclenchez un piège et subissez {damage} dégâts!")
    
    elif content["type"] == "healing_fountain":
        healing = content["healing"]
        old_hp = player.hp
        player.hp = min(player.max_hp, player.hp + healing)
        actual_healing = player.hp - old_hp
        print(f"✨ Vous buvez à la fontaine magique et récupérez {actual_healing} PV!")
    
    elif content["type"] == "stat_boost":
        stat = content["stat"]
        amount = content["amount"]
        if stat == "attack":
            player.attack += amount
            print(f"🌟 Une aura mystérieuse vous renforce! Attaque +{amount}")
        elif stat == "defense":
            player.defense += amount
            print(f"🌟 Une aura mystérieuse vous protège! Défense +{amount}")
    
    elif content["type"] == "curse":
        amount = abs(content["amount"])
        player.max_hp = max(50, player.max_hp - amount)
        player.hp = min(player.hp, player.max_hp)
        print(f"😈 Une malédiction vous affaiblit! PV max -{amount}")
    
    elif content["type"] == "experience":
        amount = content["amount"]
        player.experience += amount
        print(f"📚 Vous découvrez des connaissances anciennes! +{amount} XP")
