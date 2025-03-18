from requests import Session as RequestsSession
from fastapi import HTTPException
from sqlmodel import Session

from core.config import PRODUCTS_SERVICE_URL, USERS_SERVICE_URL
from models.order import Order
from schemas.product_schema import OrderCreate


def get_product(product_id: int):
    url = f"{PRODUCTS_SERVICE_URL}/{product_id}"
    print(url)
    response = RequestsSession().get(url)
    if response.status_code == 404:
        raise HTTPException(status_code=400, detail="Product not found")
    return response.json()


def get_user(user_id: int):
    url = f"{USERS_SERVICE_URL}/{user_id}"
    print(url)
    response = RequestsSession().get(url)
    if response.status_code == 404:
        raise HTTPException(status_code=400, detail="User not found")
    return response.json()


def get_order_by_id(session, order_id):
    obj = session.query(Order).filter(Order.id == order_id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Order not found")

    get_product(obj.product_id)
    get_user(obj.user_id)
    return obj


def get_order(session: Session, order_id: int):
    return get_order_by_id(session, order_id=order_id)


def get_orders(session: Session):
    return session.query(Order).all()


def create_order(session: Session, order: OrderCreate):
    new_order = Order(**order.model_dump())
    get_product(order.product_id)
    get_user(order.user_id)
    session.add(new_order)
    session.commit()
    session.refresh(new_order)
    return new_order