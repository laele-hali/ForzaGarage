from app.database import cars_collection
from app.schemas import CarCreate


def car_helper(car) -> dict:
    return {
        "id": str(car["_id"]),
        "manufacturer": car["manufacturer"],
        "model": car["model"],
        "model_year": car["model_year"],
        "performance_class": car["performance_class"],
        "pi": car["pi"],
        "rarity": car["rarity"],
        "drivetrain": car["drivetrain"],
        "is_new": car.get("is_new", False),
        "nickname": car.get("nickname"),
        "garage_slot": car.get("garage_slot"),
    }


async def create_car(car: CarCreate):
    car_dict = car.model_dump()
    result = await cars_collection.insert_one(car_dict)

    created_car = await cars_collection.find_one({"_id": result.inserted_id})
    return car_helper(created_car)


async def get_all_cars():
    cars = []

    async for car in cars_collection.find():
        cars.append(car_helper(car))

    return cars
