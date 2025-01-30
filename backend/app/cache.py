from aiocache import Cache

cache = Cache(Cache.MEMORY, ttl=3600)

async def get_cache(key):
    return await cache.get(key)

async def set_cache(key, value):
    await cache.set(key, value)