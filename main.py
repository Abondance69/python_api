from pokédex.pokemon import get_pokemon_info, compare_pokemon
from pokédex.type import get_pokemon_by_type

def main():
    while True:
        choice = input("Que souhaitez-vous faire ? (1: Afficher statistiques d'un Pokémon, 2: Comparer deux Pokémon, 3: Calculer stats d'un type) : ")

        if choice == '1':
            pokemon = input("Entrez le nom ou l'ID du Pokémon : ")
            get_pokemon_info(pokemon)
            break
        elif choice == '2':
            pokemon1 = input("Entrez le nom ou l'ID du premier Pokémon : ")
            pokemon2 = input("Entrez le nom ou l'ID du second Pokémon : ")
            compare_pokemon(pokemon1, pokemon2)
            break
        elif choice == '3':
            pokemon_type = input("Entrez un type de Pokémon (ex: fire, water, dragon) : ")
            get_pokemon_by_type(pokemon_type)
            break
        else:
            print("Choix invalide. Veuillez entrer 1, 2 ou 3.")

if __name__ == '__main__':
    main()
