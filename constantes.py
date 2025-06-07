
# Actions de combat
class CombatAction:
    ATTAQUER = "1"
    CAPACITE_SPECIALE = "2"
    SE_SOIGNER = "3"
    FUIR = "4"

# Actions du menu principal
class MenuAction:
    CREER_PERSONNAGE = "1"
    VOIR_STATS = "2"
    CHERCHER_MONSTRE = "3"
    EXPLORER_DONJON = "4"
    SE_REPOSER = "5"
    QUITTER = "6"

# Actions du donjon
class DungeonAction:
    AVANCER = "1"
    RECULER = "2"
    QUITTER_DONJON = "3"

# Actions du game over
class GameOverAction:
    RECOMMENCER = "1"
    QUITTER_JEU = "2"
