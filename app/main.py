from fastapi import FastAPI
from app.routers import cars

app = FastAPI(
    title="Forza Garage API",
    description="A simple API for managing a personal Forza car garage.",
    version="0.1.0",
)

app.include_router(cars.router)


@app.get("/")
def root():
    return {"message": "Forza Garage API is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
