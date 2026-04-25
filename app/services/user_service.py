from http.client import HTTPException
from sqlalchemy.orm import Session

from app.auth.utils import hash_password
from app.repository import user_repository
from app.schemas.user import UserCreateRequest, UserResponse


def create_user(db: Session, user: UserCreateRequest) -> UserResponse:
    if user_repository.get_user_by_username(db, user.username):
        raise HTTPException(status_code=400, detail="Username already exists")
    
    hashed_password = hash_password(user.password)
    
    user = user_repository.create_user(db, username=user.username, password=hashed_password)
    db.commit()
    return UserResponse.model_validate(user)