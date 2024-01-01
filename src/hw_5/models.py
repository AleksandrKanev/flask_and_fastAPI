from pydantic import BaseModel


class Cars(BaseModel):
    id: int
    brand: str
    model: str
    description: str | None = None
