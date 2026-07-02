from fastapi import APIRouter

from app.crud import create_car, get_all_cars
from app.schemas import CarCreate, CarResponse

router = APIRouter(
    prefix="/cars",
    tags=["Cars"],
)


@router.get("/", response_model=list[CarResponse])
async def get_cars():
    return await get_all_cars()


@router.post("/", response_model=CarResponse)
async def add_car(car: CarCreate):
    return await create_car(car)

