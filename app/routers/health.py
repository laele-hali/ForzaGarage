from fastapi import APIRouter

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
