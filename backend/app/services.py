import requests
import time
import asyncio
from app.config import TMDB_API_KEY, BASE_URL
from app.cache import get_cache, set_cache

max_retries = 3  # Nombre de tentatives max
delay = 3  # Délai initial

def get_movie_details(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}"
    params = {"api_key": TMDB_API_KEY, "language": "fr-FR"}

    cached_response = asyncio.run(get_cache(url))  
    if cached_response:
        print("Données récupérées du cache")
        return cached_response

    for _ in range(max_retries):
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                details = response.json()

                data = {
                    "id": details.get("id"),
                    "titre": details.get("title"),
                    "image": details.get("poster_path"),
                    "date_sortie": details.get("release_date"),
                    "popularité": details.get("popularity"),
                    "note_moyenne": details.get("vote_average")
                }

                asyncio.run(set_cache(url, data))

            if response.status_code in [429, 500, 503]:
                time.sleep(delay)

        except requests.exceptions.RequestException:
            time.sleep(delay)

    return {}

def get_popular_movies():
    url = f"{BASE_URL}/movie/popular"
    params = {"api_key": TMDB_API_KEY, "language": "fr-FR"}

    cached_response = asyncio.run(get_cache(url))
    if cached_response:
        print("Données récupérées du cache")
        return cached_response

    for _ in range(max_retries):
        try:
            response = requests.get(url, params=params)

            if response.status_code == 200:
                details = response.json()

                data = {
                    "movies": [
                        {
                            "id": movie.get("id"),
                            "titre": movie.get("title"),
                            "image": movie.get("poster_path"),
                            "date_sortie": movie.get("release_date"),
                            "popularité": movie.get("popularity"),
                            "note_moyenne": movie.get("vote_average")
                        }
                        for movie in details.get("results", [])
                    ]
                }

                asyncio.run(set_cache(url, data))
                return data

            if response.status_code in [429, 500, 503]:
                print(f"Erreur {response.status_code}. Nouvelle tentative dans {delay} secondes...")
                time.sleep(delay)

        except requests.exceptions.RequestException as e:
            print(f"Erreur réseau : {e}")
            time.sleep(delay)

    return {}

def get_now_playing_movies():
    url = f"{BASE_URL}/movie/now_playing"
    params = {"api_key": TMDB_API_KEY, "language": "fr-FR"}

    cached_response = asyncio.run(get_cache(url))
    if cached_response:
        return cached_response

    for _ in range(max_retries):
        try:
            response = requests.get(url, params=params)

            if response.status_code == 200:
                details = response.json()

                data = {
                    "movies": [
                        {
                            "id": movie.get("id"),
                            "titre": movie.get("title"),
                            "image": movie.get("poster_path"),
                            "date_sortie": movie.get("release_date"),
                            "popularité": movie.get("popularity"),
                            "note_moyenne": movie.get("vote_average")
                        }
                        for movie in details.get("results", [])
                    ]
                }

                asyncio.run(set_cache(url, data))
                return data

            if response.status_code in [429, 500, 503]:
                time.sleep(delay)

        except requests.exceptions.RequestException:
            time.sleep(delay)

    return {}

def get_upcoming_movies():
    url = f"{BASE_URL}/movie/upcoming"
    params = {"api_key": TMDB_API_KEY, "language": "fr-FR"}

    cached_response = asyncio.run(get_cache(url))
    if cached_response:
        return cached_response

    for _ in range(max_retries):
        try:
            response = requests.get(url, params=params)

            if response.status_code == 200:
                details = response.json()

                data = {
                    "movies": [
                        {
                            "id": movie.get("id"),
                            "titre": movie.get("title"),
                            "image": movie.get("poster_path"),
                            "date_sortie": movie.get("release_date"),
                            "popularité": movie.get("popularity"),
                            "note_moyenne": movie.get("vote_average")
                        }
                        for movie in details.get("results", [])
                    ]
                }

                asyncio.run(set_cache(url, data))
                return data

            if response.status_code in [429, 500, 503]:
                time.sleep(delay)

        except requests.exceptions.RequestException:
            time.sleep(delay)

    return {}

def get_top_rated_movies():
    url = f"{BASE_URL}/movie/top_rated"
    params = {"api_key": TMDB_API_KEY, "language": "fr-FR"}

    cached_response = asyncio.run(get_cache(url))
    if cached_response:
        return cached_response

    for _ in range(max_retries):
        try:
            response = requests.get(url, params=params)

            if response.status_code == 200:
                details = response.json()

                data = {
                    "movies": [
                        {
                            "id": movie.get("id"),
                            "titre": movie.get("title"),
                            "image": movie.get("poster_path"),
                            "date_sortie": movie.get("release_date"),
                            "popularité": movie.get("popularity"),
                            "note_moyenne": movie.get("vote_average")
                        }
                        for movie in details.get("results", [])
                    ]
                }

                asyncio.run(set_cache(url, data))
                return data

            if response.status_code in [429, 500, 503]:
                time.sleep(delay)

        except requests.exceptions.RequestException:
            time.sleep(delay)

    return {}
