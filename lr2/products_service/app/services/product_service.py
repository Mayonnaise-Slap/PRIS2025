from fastapi import HTTPException
from sqlmodel import Session

from models.product import Product
from repositories.product_repository import get_product_by_id, get_products, create_product
from schemas.product_schema import ProductCreate, ProductUpdate


def register_product(session: Session, product_data: ProductCreate):
    new_user = Product(**product_data.model_dump())
    return create_product(session, new_user)


def list_products(session: Session):
    return get_products(session)


def get_product(session: Session, user_id: int):
    return get_product_by_id(session, user_id)


def delete_product(session: Session, product_id: int):
    db_product = get_product_by_id(session, product_id)
    if not db_product:
        return HTTPException(status_code=404, detail="Product not found")

    session.delete(db_product)
    session.commit()
    return

def alter_product(session: Session, product_id: int, new_data: ProductUpdate):
    db_product = get_product_by_id(session, product_id)
    if not db_product:
        return HTTPException(status_code=404, detail="Product not found")

    if new_data.description:
        db_product.description = new_data.description

    if new_data.name:
        db_product.name = new_data.name

    if new_data.price:
        db_product.price = new_data.price

    session.add(db_product)
    session.commit()
    return db_product