from sqlalchemy.orm import Session
from fastapi import Depends

from fastapi import APIRouter

from app.auth.service import login_user
from app.db.dependency import get_db


router = APIRouter()

@router.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    return login_user(db, username, password)