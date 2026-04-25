from http.client import HTTPException

from sqlalchemy.orm import Session

from app.auth.utils import create_access_token, verify_password
from app.repository import user_repository

def login_user(db: Session, username: str, password: str) -> str:
    user = user_repository.get_user_by_username(db, username)

    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    token = create_access_token(data={"sub": str(user.id)})

    return {"access_token": token}