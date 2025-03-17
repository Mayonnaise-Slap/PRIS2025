import requests
from fastapi import HTTPException
from sqlmodel import Session

from core.config import PRODUCTS_SERVICE_URL, USERS_SERVICE_URL
from models.order import Order
from schemas.product_schema import OrderCreate


def get_product(product_id: int):
    response = requests.get(f"{PRODUCTS_SERVICE_URL}/{product_id}")
    if response.status_code == 404:
        raise HTTPException(status_code=400, detail="Product not found")
    return response.json()


def get_user(user_id: int):
    response = requests.get(f"{USERS_SERVICE_URL}/{user_id}")
    if response.status_code == 404:
        raise HTTPException(status_code=400, detail="User not found")
    return response.json()


def get_order_by_id(session, order_id):
    obj = session.query(Order).filter(Order.id == order_id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Order not found")
    return obj


def get_order(session: Session, order_id: int):
    return get_order_by_id(session, order_id=order_id)


def get_orders(session: Session):
    return session.query(Order).all()


def create_order(session: Session, order: OrderCreate):
    new_order = Order(**order.model_dump())
    session.add(new_order)
    session.commit()
    session.refresh(new_order)
    return new_order