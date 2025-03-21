from core.database import get_session
from fastapi import APIRouter, Depends
from schemas.user import UserCreate, UserResponse, UserUpdate
from services.user_service import register_user, list_users, get_user, alter_user, delete_user
from sqlmodel import Session

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


@router.put("/{id}", response_model=UserResponse)
def update_user_details(id: int, user_info: UserUpdate, session: Session = Depends(get_session)):
    return alter_user(session, id, user_info)


@router.delete("/{id}", response_model=UserResponse)
def delete_user_details(id: int, session: Session = Depends(get_session)):
    return delete_user(session, id)
