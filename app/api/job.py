from fastapi import APIRouter, Depends

from app.db.dependency import get_current_user, get_db
from app.services import job_service
from sqlalchemy.orm import Session
from app.schemas.job import JobCreateRequest, JobResponse


router = APIRouter()

@router.get("/jobs", response_model=list[JobResponse])
def get_jobs(company: str | None = None, status: str | None = None, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return job_service.filter_jobs(db, current_user.id, company, status)

@router.get("/jobs/{job_id}", response_model=JobResponse)
def get_job_by_id(job_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return job_service.get_job_by_id(db, current_user.id, job_id)

@router.post("/jobs", response_model=JobResponse)
def create_job(job: JobCreateRequest, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return job_service.create_job(db, current_user.id, job)

@router.delete("/jobs/{job_id}")
def delete_job(job_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return job_service.delete_job(db, current_user.id, job_id)
