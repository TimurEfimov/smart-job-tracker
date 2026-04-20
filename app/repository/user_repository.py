from app.db.models import User
from sqlalchemy.orm import Session


def get_user_by_token(db: Session, token: str) -> User:
    return db.query(User).filter(User.username == token).first()

def create_user(db: Session, username: str, password: str):
    user = User(username=username, password=password)
    db.add(user)
    db.flush()
    return user