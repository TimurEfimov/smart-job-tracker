from fastapi import FastAPI

from app.api.job import router as job_router
from app.api.user import router as user_router
from app.api.auth import router as auth_router
from app.db.database import Base, engine 

app = FastAPI()

app.include_router(job_router, prefix="/api/v1/jobs", tags=["jobs"])
app.include_router(user_router, prefix="/api/v1/users", tags=["users"])
app.include_router(auth_router, prefix="/api/v1/auth", tags=["auth"]) 

Base.metadata.create_all(bind=engine)