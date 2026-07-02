import logging

from fastapi import FastAPI

from app.routers import cars
from app.routers import health

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
)

app = FastAPI(
    title="Forza Garage API",
    description="A simple API for managing a personal Forza car garage.",
    version="0.1.0",
)

app.include_router(cars.router)
app.include_router(health.router)


@app.get("/")
def root():
    return {"message": "Forza Garage API is running"}
