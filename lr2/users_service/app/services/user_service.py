from fastapi import HTTPException
from models.users import User
from repositories.user_repository import create_user, get_users, get_user_by_id
from schemas.user import UserCreate
from sqlmodel import Session


def register_user(session: Session, user_data: UserCreate):
    new_user = User(name=user_data.name, email=user_data.email)
    return create_user(session, new_user)


def list_users(session: Session):
    return get_users(session)


def get_user(session: Session, user_id: int):
    return get_user_by_id(session, user_id)


def alter_user(session: Session, user_id: int, user_data: UserCreate):
    db_user = get_user_by_id(session, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    if user_data.name:
        db_user.name = user_data.name
    if user_data.email:
        db_user.email = user_data.email

    session.add(db_user)
    session.commit()
    return db_user


def delete_user(session: Session, user_id: int):
    user_db = get_user_by_id(session, user_id)
    if not user_db:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user_db)
    session.commit()
    return
