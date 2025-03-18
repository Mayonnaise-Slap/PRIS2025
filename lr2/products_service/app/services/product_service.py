from sqlmodel import Session

from models.product import Product
from repositories.product_repository import get_product_by_id, get_products, create_product
from schemas.product_schema import ProductCreate


def register_product(session: Session, product_data: ProductCreate):
    new_user = Product(**product_data.model_dump())
    return create_product(session, new_user)


def list_products(session: Session):
    return get_products(session)


def get_product(session: Session, user_id: int):
    return get_product_by_id(session, user_id)
