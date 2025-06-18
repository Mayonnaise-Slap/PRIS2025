from datetime import datetime

from sqlmodel import SQLModel, Field


class Order(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    user_id: int
    product_id: int
    quantity: int
    status: str
    created_at: datetime = Field(default_factory=datetime.now)
