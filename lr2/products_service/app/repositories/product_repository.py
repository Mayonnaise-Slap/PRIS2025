from fastapi import HTTPException
from sqlmodel import Session, select
from models.product import Product

def create_product(session: Session, product: Product):
    session.add(product)
    session.commit()
    session.refresh(product)
    return product

def get_products(session: Session):
    return session.exec(select(Product)).all()


def get_product_by_id(session: Session, id: int):
    obj = session.exec(select(Product).where(Product.id == id)).first()
    if not obj:
        raise HTTPException(status_code=404, detail=f"Product not found")
    return obj
