from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    mongo_url: str = "mongodb://localhost:27017"
    mongo_db_name: str = "forza_garage"

    redis_host: str = "localhost"
    redis_port: int = 6379
    redis_cache_ttl: int = 300

    class Config:
        env_file = ".env"


settings = Settings()
