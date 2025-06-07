import random
from character import Character
from monster import Monster, create_dungeon_monster
from classes import get_available_classes, display_classes
from dungeon import create_dungeon, explore_room




def create_monster(level):
    monsters = [
        ("Gobelin", 30, 15, 5, 25, 15),
        ("Orc", 50, 20, 8, 40, 25),
        ("Troll", 80, 25, 12, 60, 40),
        ("Dragon", 120, 35, 15, 100, 75)
    ]
    
    base_monster = random.choice(monsters)
    name, hp, attack, defense, exp, gold = base_monster
    
    # Ajuste les stats selon le niveau
    level_modifier = level - 1
    hp += level_modifier * 10
    attack += level_modifier * 3
    defense += level_modifier * 2
    exp += level_modifier * 10
    gold += level_modifier * 5
    
    return Monster(name, hp, attack, defense, exp, gold)

def combat(player, monster):
    print(f"\n⚔️  Combat contre {monster.name}!")
    print(f"{monster.name}: {monster.hp} PV, {monster.attack} ATT, {monster.defense} DEF")
    
    while player.hp > 0 and monster.hp > 0:
        print(f"\n--- Tour de combat ---")
        print(f"Vos PV: {player.hp}/{player.max_hp}")
        print(f"PV de {monster.name}: {monster.hp}/{monster.max_hp}")
        
        action = input("\nQue voulez-vous faire? (1: Attaquer, 2: Capacité spéciale, 3: Se soigner, 4: Fuir): ")
        
        match action:
            case "1":
                player.attack_monster(monster)
                if monster.hp <= 0:
                    print(f"\n🎉 Vous avez vaincu {monster.name}!")
                    player.experience += monster.exp_reward
                    player.gold += monster.gold_reward
                    print(f"Vous gagnez {monster.exp_reward} XP et {monster.gold_reward} or!")
                    
                    if player.experience >= player.level * 100:
                        player.experience -= player.level * 100
                        player.level_up()
                    return True
                
                monster.attack_player(player)
                
            case "2":
                if player.use_special_ability(monster):
                    if monster.hp <= 0:
                        print(f"\n🎉 Vous avez vaincu {monster.name}!")
                        player.experience += monster.exp_reward
                        player.gold += monster.gold_reward
                        print(f"Vous gagnez {monster.exp_reward} XP et {monster.gold_reward} or!")
                        
                        if player.experience >= player.level * 100:
                            player.experience -= player.level * 100
                            player.level_up()
                        return True
                    monster.attack_player(player)
                else:
                    continue  # Ne pas faire attaquer le monstre si la capacité n'a pas été utilisée
                
            case "3":
                player.heal()
                monster.attack_player(player)
                
            case "4":
                print("Vous fuyez le combat!")
                return False
        
        if player.hp <= 0:
            print(f"\n💀 {player.name} est mort!")
            return False
        
        # Réduire les temps de recharge à chaque tour
        player.reduce_cooldowns()
    
    return True

def explore_dungeon(player):
    """Fonction principale d'exploration de donjon"""
    dungeon = create_dungeon(player.level)
    print(f"\n🏰 Vous entrez dans: {dungeon.name}")
    print(f"Le donjon contient {len(dungeon.rooms)} salles à explorer.")
    
    while not dungeon.completed:
        current_room = dungeon.get_current_room()
        print(f"\n--- Salle {dungeon.current_room + 1}/{len(dungeon.rooms)} ---")
        
        # Explorer la salle actuelle
        explore_room(player, current_room)
        
        # Vérifier si c'est un combat
        if current_room.content and current_room.content.get("type") in ["dungeon_monster", "boss_monster"]:
            difficulty = current_room.content["difficulty"]
            monster = create_dungeon_monster(difficulty, player.level)
            print(f"\n⚔️ Un {monster.name} apparaît!")
            
            combat_result = combat(player, monster)
            if not combat_result:
                if player.hp <= 0:
                    print("💀 Vous êtes mort dans le donjon...")
                    return False
                else:
                    print("Vous fuyez le donjon!")
                    return True
        
        # Vérifier si le joueur est mort à cause d'un piège
        if player.hp <= 0:
            print("💀 Vous succombez aux dangers du donjon...")
            return False
        
        # Menu d'actions dans le donjon
        if dungeon.current_room == len(dungeon.rooms) - 1:
            print("\n🎉 Félicitations! Vous avez terminé le donjon!")
            bonus_exp = 100 + (player.level * 20)
            bonus_gold = 75 + (player.level * 15)
            player.experience += bonus_exp
            player.gold += bonus_gold
            print(f"Récompense de fin: +{bonus_exp} XP et +{bonus_gold} or!")
            dungeon.completed = True
            break
        
        print(f"\nQue voulez-vous faire?")
        print("1. Avancer vers la prochaine salle")
        if dungeon.can_retreat():
            print("2. Reculer vers la salle précédente")
        print("3. Quitter le donjon")
        
        choice = input("Votre choix: ")
        
        match choice:
            case "1":
                if dungeon.advance_room():
                    print("Vous avancez vers la prochaine salle...")
                else:
                    print("Vous ne pouvez pas aller plus loin!")
            
            case "2" if dungeon.can_retreat():
                dungeon.retreat_room()
                print("Vous reculez vers la salle précédente...")
            
            case "3":
                print("Vous quittez le donjon.")
                return True
        
        # Vérifier level up
        if player.experience >= player.level * 100:
            player.experience -= player.level * 100
            player.level_up()
    
    return True


def main_menu():
    print("\n=== JEU RPG ===")
    print("1. Créer un personnage")
    print("2. Voir les statistiques")
    print("3. Chercher un monstre")
    print("4. Explorer un donjon")
    print("5. Se reposer (récupère tous les PV)")
    print("6. Quitter")
    return input("Choisissez une option: ")

def create_new_character():
    """Fonction pour créer un nouveau personnage"""
    player_name = input("Entrez le nom de votre personnage: ")
    display_classes()
    class_choice = input("Choisissez une classe (1-5): ")
    
    classes = get_available_classes()
    selected_class = classes.get(class_choice)
    
    if selected_class:
        player = Character(player_name, selected_class)
        print(f"\nBienvenue, {player.name} le {selected_class.name}! Votre aventure commence...")
    else:
        player = Character(player_name)
        print(f"\nClasse invalide. Bienvenue, {player.name}! Votre aventure commence...")
    
    player.display_stats()
    return player

def game_over_menu():
    """Menu affiché après un Game Over"""
    print("\n💀 GAME OVER 💀")
    print("Votre aventure se termine ici...")
    print("\nQue voulez-vous faire?")
    print("1. Recommencer une nouvelle partie")
    print("2. Quitter le jeu")
    return input("Votre choix: ")

def main():
    print("🏰 Bienvenue dans le monde RPG! 🏰")
    
    # Boucle principale du jeu
    while True:
        player = create_new_character()
        
        # Boucle de jeu pour ce personnage
        while player.hp > 0:
            choice = main_menu()
            
            match choice:
                case "1":
                    player = create_new_character()
                    
                case "2":
                    player.display_stats()
                    
                case "3":
                    monster = create_monster(player.level)
                    combat_result = combat(player, monster)
                    if not combat_result and player.hp <= 0:
                        break
                        
                case "4":
                    dungeon_result = explore_dungeon(player)
                    if not dungeon_result and player.hp <= 0:
                        break
                        
                case "5":
                    player.hp = player.max_hp
                    print(f"{player.name} se repose et récupère tous ses PV!")
                    
                case "6":
                    print("Merci d'avoir joué! À bientôt!")
                    return
                
                case _:
                    print("Option invalide!")
        
        # Le joueur est mort, afficher le menu Game Over
        if player.hp <= 0:
            game_over_choice = game_over_menu()
            
            match game_over_choice:
                case "1":
                    print("\n🔄 Nouvelle partie commencée!")
                    continue  # Recommencer la boucle principale
                case "2":
                    print("Merci d'avoir joué! À bientôt!")
                    break
                case _:
                    print("Choix invalide. Fin du jeu.")
                    break

if __name__ == "__main__":
    main()
