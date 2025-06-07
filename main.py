import random
from character import Character
from monster import Monster
from classes import get_available_classes, display_classes




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
        
        if action == "1":
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
            
        elif action == "2":
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
            
        elif action == "3":
            player.heal()
            monster.attack_player(player)
            
        elif action == "4":
            print("Vous fuyez le combat!")
            return False
        
        if player.hp <= 0:
            print(f"\n💀 {player.name} est mort!")
            return False
        
        # Réduire les temps de recharge à chaque tour
        player.reduce_cooldowns()
    
    return True

def main_menu():
    print("\n=== JEU RPG ===")
    print("1. Créer un personnage")
    print("2. Voir les statistiques")
    print("3. Chercher un monstre")
    print("4. Se reposer (récupère tous les PV)")
    print("5. Quitter")
    return input("Choisissez une option: ")

def main():
    print("🏰 Bienvenue dans le monde RPG! 🏰")
    
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
    
    while player.hp > 0:
        choice = main_menu()
        
        if choice == "1":
            player_name = input("Entrez le nom de votre nouveau personnage: ")
            display_classes()
            class_choice = input("Choisissez une classe (1-5): ")
            
            classes = get_available_classes()
            selected_class = classes.get(class_choice)
            
            if selected_class:
                player = Character(player_name, selected_class)
                print(f"Nouveau personnage {player.name} ({selected_class.name}) créé!")
            else:
                player = Character(player_name)
                print(f"Classe invalide. {player.name} créé sans classe.")
            
            player.display_stats()
            
        elif choice == "2":
            player.display_stats()
            
        elif choice == "3":
            monster = create_monster(player.level)
            combat_result = combat(player, monster)
            if not combat_result and player.hp <= 0:
                break
                
        elif choice == "4":
            player.hp = player.max_hp
            print(f"{player.name} se repose et récupère tous ses PV!")
            
        elif choice == "5":
            print("Merci d'avoir joué! À bientôt!")
            break
        
        else:
            print("Option invalide!")
    
    if player.hp <= 0:
        print("\n💀 GAME OVER 💀")
        print("Votre aventure se termine ici...")

if __name__ == "__main__":
    main()
