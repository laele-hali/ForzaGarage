from fastapi import APIRouter, HTTPException

from app.crud import create_car, get_all_cars, get_car_by_id
from app.schemas import CarCreate, CarResponse

router = APIRouter(
    prefix="/cars",
    tags=["Cars"],
)


@router.get("/", response_model=list[CarResponse])
async def get_cars():
    return await get_all_cars()


@router.get("/{car_id}", response_model=CarResponse)
async def get_car(car_id: str):
    car = await get_car_by_id(car_id)

    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")

    return car


@router.post("/", response_model=CarResponse)
async def add_car(car: CarCreate):
    return await create_car(car)
