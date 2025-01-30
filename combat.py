import random
from pokédex.pokemon import get_pokemon_info

def calculer_degats(attacker_attack, defender_defense):
    """Calculer les dégâts infligés lors d'une attaque en fonction de l'attaque de l'attaquant et de la défense du défenseur"""
    return max(1, attacker_attack - defender_defense)

def simuler_combat(pokemon1, pokemon2):
    # Récupérer les statistiques des deux Pokémon
    print(f"\nStatistiques de {pokemon1}:")
    hp1, attack1 = get_pokemon_info(pokemon1)

    print(f"\nStatistiques de {pokemon2}:")
    hp2, attack2 = get_pokemon_info(pokemon2)

    # Vérifier si les statistiques ont bien été récupérées
    if hp1 is None or hp2 is None:
        return

    # Initialiser les points de vie restants
    pv_pokemon1 = hp1
    pv_pokemon2 = hp2

    # Variables pour suivre les dégâts infligés
    degats_totaux_pokemon1 = 0
    degats_totaux_pokemon2 = 0

    # Simuler 5 tours de combat
    for tour in range(1, 6):
        print(f"\n--- Tour {tour} ---")

        # Pokémon 1 attaque Pokémon 2
        degats1 = calculer_degats(attack1, hp2)  # Attack1 inflige des dégâts en fonction de la défense de pokemon2
        degats_totaux_pokemon1 += degats1
        pv_pokemon2 -= degats1
        print(f"{pokemon1} inflige {degats1} dégâts à {pokemon2}. PV restants de {pokemon2}: {pv_pokemon2}")

        # Si le Pokémon 2 est KO, le combat se termine
        if pv_pokemon2 <= 0:
            print(f"\n{pokemon2} est KO! {pokemon1} remporte le combat.")
            return

        # Pokémon 2 attaque Pokémon 1
        degats2 = calculer_degats(attack2, hp1)  # Attack2 inflige des dégâts en fonction de la défense de pokemon1
        degats_totaux_pokemon2 += degats2
        pv_pokemon1 -= degats2
        print(f"{pokemon2} inflige {degats2} dégâts à {pokemon1}. PV restants de {pokemon1}: {pv_pokemon1}")

        # Si le Pokémon 1 est KO, le combat se termine
        if pv_pokemon1 <= 0:
            print(f"\n{pokemon1} est KO! {pokemon2} remporte le combat.")
            return

    # Si les deux Pokémon survivent après 5 tours, déterminer le gagnant en fonction des dégâts infligés
    print("\n--- Fin du combat ---")
    print(f"\nDégâts totaux de {pokemon1}: {degats_totaux_pokemon1}")
    print(f"Dégâts totaux de {pokemon2}: {degats_totaux_pokemon2}")

    if degats_totaux_pokemon1 > degats_totaux_pokemon2:
        print(f"\n{pokemon1} remporte le combat!")
    elif degats_totaux_pokemon2 > degats_totaux_pokemon1:
        print(f"\n{pokemon2} remporte le combat!")
    else:
        print("\nLe combat se termine par un match nul!")

if __name__ == "__main__":
    # Demander à l'utilisateur d'entrer les noms ou IDs des Pokémon
    pokemon1 = input("Entrez le nom ou l'ID du premier Pokémon : ")
    pokemon2 = input("Entrez le nom ou l'ID du second Pokémon : ")

    # Simuler le combat
    simuler_combat(pokemon1, pokemon2)
