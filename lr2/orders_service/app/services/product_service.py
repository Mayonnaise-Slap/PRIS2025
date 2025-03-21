from core.config import PRODUCTS_SERVICE_URL, USERS_SERVICE_URL
from fastapi import HTTPException
from models.order import Order
from requests import Session as RequestsSession
from schemas.product_schema import OrderCreate, OrderUpdate
from sqlmodel import Session



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


def alter_order(session: Session, order_id: int, order_data: OrderUpdate):
    db_order = get_order(session, order_id)
    if not db_order:
        return HTTPException(status_code=404, detail="Order not found")
    if order_data.user_id:
        get_user(order_data.user_id)
        db_order.user_id = order_data.user_id

    if order_data.product_id:
        get_product(order_data.product_id)
        db_order.product_id = order_data.product_id

    if order_data.quantity:
        db_order.quantity = order_data.quantity
    if order_data.status:
        db_order.status = order_data.status

    session.add(db_order)
    session.commit()
    return db_order


def delete_order(session: Session, order_id: int):
    db_order = get_order(session, order_id)
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    session.delete(db_order)
    session.commit()
    return
