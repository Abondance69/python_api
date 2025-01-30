import requests

def get_pokemon_info(pokemon_id_or_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id_or_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        name = data['name']
        hp = data['stats'][0]['base_stat']
        attack = data['stats'][1]['base_stat']
        defense = data['stats'][2]['base_stat']
        print(f"\nStatistiques de {name} :")
        print(f"Points de Vie (HP) : {hp}")
        print(f"Attaque : {attack}")
        print(f"Défense : {defense}")
        return hp, attack
    else:
        print(f"Erreur : Impossible de récupérer les données pour {pokemon_id_or_name}")
        return None, None

def compare_pokemon(pokemon1, pokemon2):
    print("\nComparaison des Pokémon:")
    hp1, attack1 = get_pokemon_info(pokemon1)
    hp2, attack2 = get_pokemon_info(pokemon2)

    if hp1 is not None and hp2 is not None:
        print("\nLe Pokémon avec le plus de points de vie (HP) et d'attaque est :")
        if hp1 > hp2 and attack1 > attack2:
            print(f"{pokemon1} est plus fort")
        elif hp2 > hp1 and attack2 > attack1:
            print(f"{pokemon2} est plus fort")
        else:
            print("Les deux Pokémon sont similaires en termes de statistiques.")
