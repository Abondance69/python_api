import requests
import time
from app.config import TMDB_API_KEY, BASE_URL

max_retries=3 # nombre de tentative
delay=3 # delai en seconde

def get_movie_details(movie_id) :
    url = f"{BASE_URL}/movie/{movie_id}"
    params = {"api_key": TMDB_API_KEY, "language": "fr-FR"}

    for _ in range(max_retries) :
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200 :
                data = response.json()
                return {
                    "id" : data.get("id"),
                    "titre": data.get("title"),
                    "date_sortie": data.get("release_date"),
                    "popularité": data.get("popularity"),
                    "note_moyenne": data.get("vote_average")
                }

            if response.status_code in [429, 500, 503] :
                time.sleep(delay)
                delay *= 2

            if response.status_code in [400, 401, 403, 404]:
                return {"erreur": f"Erreur {response.status_code}"}

        except requests.exceptions.RequestException :
            time.sleep(delay)

    return {"erreur": "Échec après plusieurs tentatives."}

def get_popular_movies():
    url = f"{BASE_URL}/movie/popular"
    params = {"api_key": TMDB_API_KEY, "language": "fr-FR"}
    
    for _ in range(max_retries) :
        try:
            response = requests.get(url, params=params)

            if response.status_code == 200:
                data = response.json()
                popular_movies = []

                # On parcourt les films populaires
                for movie in data.get("results", []):
                    popular_movies.append({
                        "titre": movie.get("title"),
                        "image": movie.get("poster_path"),
                        "date_sortie": movie.get("release_date"),
                        "popularité": movie.get("popularity"),
                        "note_moyenne": movie.get("vote_average")
                    })

                return {"movies": popular_movies}

            elif response.status_code in [429, 500, 503]:
                print(f"Erreur {response.status_code}. Nouvelle tentative dans {delay} secondes...")
                time.sleep(delay)
                delay *= 2
    
            elif response.status_code in [400, 401, 403, 404]:
                return {"erreur": f"Erreur {response.status_code}: {response.json().get('status_message', 'Problème inconnu')}"}

        except requests.exceptions.RequestException as e:
            print(f"Erreur réseau : {e}")
            time.sleep(delay)  # Pause avant de réessayer
    
    return {"erreur": "Échec après plusieurs tentatives."}

def get_now_playing_movies():
    url = f"{BASE_URL}/movie/now_playing"
    params = {"api_key": TMDB_API_KEY, "language": "fr-FR"}
    
    for _ in range(max_retries) :
        try:
            response = requests.get(url, params=params)

            if response.status_code == 200:
                data = response.json()
                now_playing = []

                # On parcourt les films populaires
                for movie in data.get("results", []):
                    now_playing.append({
                        "titre": movie.get("title"),
                        "image": movie.get("poster_path"),
                        "date_sortie": movie.get("release_date"),
                        "popularité": movie.get("popularity"),
                        "note_moyenne": movie.get("vote_average")
                    })

                return {"movies": now_playing}
                # return data

            elif response.status_code in [429, 500, 503]:
                print(f"Erreur {response.status_code}. Nouvelle tentative dans {delay} secondes...")
                time.sleep(delay)
                delay *= 2
    
            elif response.status_code in [400, 401, 403, 404]:
                return {"erreur": f"Erreur {response.status_code}: {response.json().get('status_message', 'Problème inconnu')}"}

        except requests.exceptions.RequestException as e:
            print(f"Erreur réseau : {e}")
            time.sleep(delay)  # Pause avant de réessayer
    
    return {"erreur": "Échec après plusieurs tentatives."}

def get_upcoming_movies():
    url = f"{BASE_URL}/movie/upcoming"
    params = {"api_key": TMDB_API_KEY, "language": "fr-FR"}
    
    for _ in range(max_retries) :
        try:
            response = requests.get(url, params=params)

            if response.status_code == 200:
                data = response.json()
                upcoming = []

                # On parcourt les films populaires
                for movie in data.get("results", []):
                    upcoming.append({
                        "titre": movie.get("title"),
                        "image": movie.get("poster_path"),
                        "date_sortie": movie.get("release_date"),
                        "popularité": movie.get("popularity"),
                        "note_moyenne": movie.get("vote_average")
                    })

                return {"movies": upcoming}

            elif response.status_code in [429, 500, 503]:
                print(f"Erreur {response.status_code}. Nouvelle tentative dans {delay} secondes...")
                time.sleep(delay)
                delay *= 2
    
            elif response.status_code in [400, 401, 403, 404]:
                return {"erreur": f"Erreur {response.status_code}: {response.json().get('status_message', 'Problème inconnu')}"}

        except requests.exceptions.RequestException as e:
            print(f"Erreur réseau : {e}")
            time.sleep(delay)  # Pause avant de réessayer
    
    return {"erreur": "Échec après plusieurs tentatives."}

def get_top_rated_movies():
    url = f"{BASE_URL}/movie/top_rated"
    params = {"api_key": TMDB_API_KEY, "language": "fr-FR"}

    for _ in range(max_retries) :
        try:
            response = requests.get(url, params=params)

            if response.status_code == 200:
                data = response.json()
                top_rated = []

                # On parcourt les films populaires
                for movie in data.get("results", []):
                    top_rated.append({
                        "titre": movie.get("title"),
                        "image": movie.get("poster_path"),
                        "date_sortie": movie.get("release_date"),
                        "popularité": movie.get("popularity"),
                        "note_moyenne": movie.get("vote_average")
                    })

                return {"movies": top_rated}

            elif response.status_code in [429, 500, 503]:
                print(f"Erreur {response.status_code}. Nouvelle tentative dans {delay} secondes...")
                time.sleep(delay)
                delay *= 2
    
            elif response.status_code in [400, 401, 403, 404]:
                return {"erreur": f"Erreur {response.status_code}: {response.json().get('status_message', 'Problème inconnu')}"}

        except requests.exceptions.RequestException as e:
            print(f"Erreur réseau : {e}")
            time.sleep(delay)  # Pause avant de réessayer
    
    return {"erreur": "Échec après plusieurs tentatives."}