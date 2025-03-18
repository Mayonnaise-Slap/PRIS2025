from fastapi import APIRouter, Depends
from sqlmodel import Session
from core.database import get_session
from schemas.product_schema import OrderResponse, OrderCreate
from services.product_service import create_order, get_order, get_orders, alter_order, delete_order

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
def get_user_details(id: int, session: Session = Depends(get_session)):
    return alter_order(session, id)

@router.delete("/{id}", response_model=OrderResponse)
def delete_user_details(id: int, session: Session = Depends(get_session)):
    return delete_order(session, id)
