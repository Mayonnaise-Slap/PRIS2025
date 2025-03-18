from fastapi import HTTPException
from sqlmodel import Session, select
from models.users import User

def create_user(session: Session, user: User):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def get_users(session: Session):
    return session.exec(select(User)).all()


def get_user_by_id(session: Session, id: int):
    obj =  session.exec(select(User).where(User.id == id)).first()
    if not obj:
        raise HTTPException(status_code=404, detail=f"User not found")
    return obj
