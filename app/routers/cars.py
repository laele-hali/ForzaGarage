from fastapi import APIRouter

router = APIRouter(
    prefix="/cars",
    tags=["Cars"],
)


@router.get("/")
def get_cars():
    return {"message": "List of cars will go here"}
