from http.client import HTTPException
from typing import Generator
from fastapi.params import Depends
from sqlalchemy.orm import Session

from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.db.database import SessionLocal
from app.repository import user_repository
from app.schemas.user import UserResponse

security = HTTPBearer()


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(credentails: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)) ->   UserResponse:
    token = credentails.credentials
    user = user_repository.get_user_by_token(db, token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    return UserResponse.model_validate(user)