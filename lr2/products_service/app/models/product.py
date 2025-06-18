from sqlmodel import SQLModel, Field


class Product(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    description: str = Field(nullable=False)
    name: str = Field(nullable=False)
    price: float = Field(nullable=False)
