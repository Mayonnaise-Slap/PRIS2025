from fastapi import APIRouter, Depends
from sqlmodel import Session
from core.database import get_session
from services.user_service import register_user, list_users, get_user
from schemas.user import UserCreate, UserResponse

router = APIRouter()

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, session: Session = Depends(get_session)):
    return register_user(session, user)

@router.get("/", response_model=list[UserResponse])
def get_users(session: Session = Depends(get_session)):
    return list_users(session)

@router.get("/{id}", response_model=UserResponse)
def get_user_details(id: int, session: Session = Depends(get_session)):
    return get_user(session, id)
