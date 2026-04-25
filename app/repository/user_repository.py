from app.db.models import User
from sqlalchemy.orm import Session


def get_user_by_id(db: Session, user_id: int) -> User:
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, username: str, password: str):
    user = User(username=username, password=password)
    db.add(user)
    db.flush()
    return user

def get_user_by_username(db: Session, username: str) -> User:
    return db.query(User).filter(User.username == username).first()