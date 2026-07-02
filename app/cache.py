import json

import redis.asyncio as redis

from app.config import settings

redis_client = redis.Redis(
    host=settings.redis_host,
    port=settings.redis_port,
    decode_responses=True,
)


async def get_cache(key: str):
    data = await redis_client.get(key)

    if data:
        print(f"✅ Cache HIT: {key}")
        return json.loads(data)

    print(f"❌ Cache MISS: {key}")
    return None


async def set_cache(key: str, value):
    await redis_client.set(
        key,
        json.dumps(value),
        ex=settings.redis_cache_ttl,
    )
