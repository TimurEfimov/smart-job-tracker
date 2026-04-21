from http.client import HTTPException
from sqlalchemy.orm import Session

from app.repository import user_repository
from app.schemas.user import UserCreateRequest, UserResponse


def create_user(db: Session, user: UserCreateRequest) -> UserResponse:
    if user_repository.get_user_by_token(db, user.username):
        raise HTTPException(status_code=400, detail="Username already exists")
    
    user = user_repository.create_user(db, username=user.username, password=user.password)
    db.commit()
    return UserResponse.model_validate(user)