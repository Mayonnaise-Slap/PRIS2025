from core.database import get_session
from fastapi import APIRouter, Depends
from schemas.product_schema import OrderResponse, OrderCreate, OrderUpdate
from services.product_service import create_order, get_order, get_orders, alter_order, delete_order
from sqlmodel import Session

router = APIRouter()


@router.post("/", response_model=OrderResponse)
def create_user(user: OrderCreate, session: Session = Depends(get_session)):
    return create_order(session, user)


@router.get("/", response_model=list[OrderResponse])
def get_users(session: Session = Depends(get_session)):
    return get_orders(session)


@router.get("/{id}", response_model=OrderResponse)
def get_user_details(id: int, session: Session = Depends(get_session)):
    return get_order(session, id)


@router.put("/{id}", response_model=OrderResponse)
def get_user_details(id: int, order_data: OrderUpdate, session: Session = Depends(get_session)):
    return alter_order(session, id, order_data)


@router.delete("/{id}", response_model=OrderResponse)
def delete_user_details(id: int, session: Session = Depends(get_session)):
    return delete_order(session, id)
