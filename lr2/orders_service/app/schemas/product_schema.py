from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class OrderCreate(BaseModel):
    user_id: int
    product_id: int
    quantity: int
    status: str


class OrderResponse(BaseModel):
    id: int
    user_id: int
    product_id: int
    quantity: int
    status: str
    created_at: datetime
    user: Optional[dict] = None
    product: Optional[dict] = None

class OrderUpdate(BaseModel):
    user_id: Optional[int] = None
    product_id: Optional[int] = None
    quantity: Optional[int] = None
    status: Optional[str] = None