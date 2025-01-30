import os
from dotenv import load_dotenv

load_dotenv()

TMDB_API_KEY = os.getenv("APP_API_KEY")
BASE_URL = os.getenv("APP_URL_API_SITE")
SERVER_URL = os.getenv("SERVER_URL")

if not TMDB_API_KEY:
    raise ValueError("La clé API TMDB est absente ! Vérifie ton fichier .env")
