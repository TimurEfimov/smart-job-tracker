from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.db.dependency import get_db, get_current_user
from app.schemas.user import UserCreateRequest, UserResponse
from app.services import user_service


router = APIRouter()

@router.post("/register", response_model=UserResponse)
def create_user(payload: UserCreateRequest, db: Session = Depends(get_db)):
    return user_service.create_user(db, payload)

@router.get("/me", response_model=UserResponse)
def get_current_user(current_user = Depends(get_current_user)):
    return current_user