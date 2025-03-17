from fastapi import APIRouter, Depends
from sqlmodel import Session
from core.database import get_session
from services.product_service import register_product, list_products, get_product
from schemas.product_schema import ProductCreate, ProductResponse

router = APIRouter()

@router.post("/", response_model=ProductResponse)
def create_user(user: ProductCreate, session: Session = Depends(get_session)):
    return register_product(session, user)

@router.get("/", response_model=list[ProductResponse])
def get_users(session: Session = Depends(get_session)):
    return list_products(session)

@router.get("/{id}", response_model=ProductResponse)
def get_user_details(id: int, session: Session = Depends(get_session)):
    return get_product(session, id)
