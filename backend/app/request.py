import aiohttp
import asyncio
from config import SERVER_URL
from app.cache import get_cache, set_cache

MAX_CONCURRENT_REQUESTS = 10
retries = 3
delay = 3

async def fetch(session, url, semaphore):
    """Effectue une requête GET avec gestion des erreurs et mise en cache."""
    
    cached_response = await get_cache(url)
    if cached_response:
        return cached_response
    
    for attempt in range(retries):
        async with semaphore:
            try:
                async with session.get(url) as response:
                    if response.status == 200:
                        data = await response.json()
                        await set_cache(url, data)  # stocker la réponse en cache
                        return data
                    elif response.status in [429, 500, 503]:
                        await asyncio.sleep(delay)
                        delay *= 2
                    else:
                        return {"erreur": f"Erreur {response.status} sur {url}"}
            except aiohttp.ClientError as e:
                await asyncio.sleep(delay)
                delay *= 2  

    return {"erreur": f"Échec après {retries} tentatives sur {url}"}

async def fetch_all(urls):
    semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url, semaphore) for url in urls]
        return await asyncio.gather(*tasks)

async def simulation():
    urls = [
        f"{SERVER_URL}/api/movie/550",
        f"{SERVER_URL}/api/movie/popular",
        f"{SERVER_URL}/api/movie/now_playing",
        f"{SERVER_URL}/api/movie/top_rated",
        f"{SERVER_URL}/api/movie/upcoming",
    ]

    results = await fetch_all(urls)
    print(results)

asyncio.run(simulation())