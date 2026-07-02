from fastapi import APIRouter

from app.cache import redis_client
from app.database import database

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("/")
def health():
    return {"status": "ok"}


@router.get("/db")
async def database_health():
    await database.command("ping")
    return {"database": "ok"}


@router.get("/redis")
async def redis_health():
    await redis_client.ping()
    return {"redis": "ok"}
