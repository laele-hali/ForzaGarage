from pydantic import BaseModel, Field


class CarCreate(BaseModel):
    manufacturer: str
    model: str
    model_year: int = Field(..., ge=1886)
    performance_class: str = Field(..., pattern="^(D|C|B|A|S1|S2|X)$")
    pi: int = Field(..., ge=100, le=999)
    rarity: str
    drivetrain: str
    is_new: bool = False
    nickname: str | None = None
    garage_slot: int | None = Field(default=None, ge=1)


class CarResponse(CarCreate):
    id: str
