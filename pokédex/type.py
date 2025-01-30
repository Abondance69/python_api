import requests
from pokédex.pokemon import get_pokemon_info

def get_pokemon_by_type(pokemon_type):
    url = f"https://pokeapi.co/api/v2/type/{pokemon_type}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        pokemons = data['pokemon']
        num_pokemons = len(pokemons)
        total_hp = 0
        print(f"\nListe des Pokémon de type {pokemon_type}:")

        for pokemon in pokemons[:5]:  
            pokemon_name = pokemon['pokemon']['name']
            hp, _ = get_pokemon_info(pokemon_name)
            if hp is not None:
                total_hp += hp

        if num_pokemons > 0:
            average_hp = total_hp / num_pokemons
            print(f"\nNombre de Pokémon de type {pokemon_type}: {num_pokemons}")
            print(f"Moyenne des Points de Vie (HP) des Pokémon de type {pokemon_type}: {average_hp:.2f}")
        else:
            print(f"Aucun Pokémon trouvé pour le type {pokemon_type}.")
    else:
        print(f"Erreur : Impossible de récupérer les données pour le type {pokemon_type}.")
