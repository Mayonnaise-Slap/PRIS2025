from sqlmodel import Session
from models.users import User
from schemas.user import UserCreate
from repositories.user_repository import create_user, get_users, get_user_by_id

def register_user(session: Session, user_data: UserCreate):
    new_user = User(name=user_data.name, email=user_data.email)
    return create_user(session, new_user)

def list_users(session: Session):
    return get_users(session)

def get_user(session: Session, user_id: int):
    return get_user_by_id(session, user_id)