from fastapi import APIRouter

from app.crud import create_car
from app.schemas import CarCreate, CarResponse

router = APIRouter(
    prefix="/cars",
    tags=["Cars"],
)


@router.get("/")
def get_cars():
    return {"message": "List of cars will go here"}


@router.post("/", response_model=CarResponse)
async def add_car(car: CarCreate):
    return await create_car(car)
