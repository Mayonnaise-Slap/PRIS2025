from pydantic import BaseModel


class ProductCreate(BaseModel):
    description: str
    name: str
    price: float


class ProductResponse(BaseModel):
    id: int
    description: str
    name: str
    price: float
