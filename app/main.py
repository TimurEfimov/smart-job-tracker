from fastapi import FastAPI

from app.api.job import router as job_router
from app.api.user import router as user_router
from app.db.database import Base, engine 

app = FastAPI()

app.include_router(job_router, prefix="/api/v1", tags=["jobs"])
app.include_router(user_router, prefix="/api/v1", tags=["users"])

Base.metadata.create_all(bind=engine)