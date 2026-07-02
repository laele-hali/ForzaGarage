import json
import logging

import redis.asyncio as redis

from app.config import settings

logger = logging.getLogger("forza_garage.cache")

redis_client = redis.Redis(
    host=settings.redis_host,
    port=settings.redis_port,
    decode_responses=True,
)


async def get_cache(key: str):
    data = await redis_client.get(key)

    if data:
        logger.info("Cache HIT for key: %s", key)
        return json.loads(data)

    logger.info("Cache MISS for key: %s", key)
    return None


async def set_cache(key: str, value):
    await redis_client.set(
        key,
        json.dumps(value),
        ex=settings.redis_cache_ttl,
    )

    logger.info(
        "Stored key in Redis: %s with TTL: %s seconds",
        key,
        settings.redis_cache_ttl,
    )


async def delete_cache(key: str):
    await redis_client.delete(key)
    logger.info("Deleted Redis cache key: %s", key)
