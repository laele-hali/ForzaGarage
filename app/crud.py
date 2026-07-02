from app.database import cars_collection
from app.schemas import CarCreate


async def create_car(car: CarCreate):
    car_dict = car.model_dump()
    result = await cars_collection.insert_one(car_dict)

    car_dict["id"] = str(result.inserted_id)
    return car_dict
