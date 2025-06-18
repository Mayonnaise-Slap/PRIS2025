from typing import Optional

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


class ProductUpdate(BaseModel):
    description: Optional[str] = None
    name: Optional[str] = None
    price: Optional[float] = None
