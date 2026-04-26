from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repository import job_repository
from app.schemas.job import JobCreateRequest, JobResponse

def get_job_by_id(db: Session, user_id: int, job_id: int) -> JobResponse:
    if not job_repository.is_job_exists(db, user_id, job_id):
        raise HTTPException(status_code=404, detail="Job not found")
    
    job = job_repository.get_job_by_id(db, user_id, job_id)
    return JobResponse.model_validate(job)

def create_job(db: Session, user_id: int, job: JobCreateRequest) -> JobResponse:
    job = job_repository.create_job(db, user_id=user_id, title=job.title, company=job.company, status=job.status)
    db.commit()
    return JobResponse.model_validate(job)

def delete_job(db: Session, user_id: int, job_id: int):
    if not job_repository.is_job_exists(db, user_id, job_id):
        raise HTTPException(status_code=404, detail="Job not found")
    
    job_repository.delete_job(db, user_id, job_id)

    db.commit()

    return {
        "detail": f"Job {job_id} deleted successfully"
    }

def filter_jobs(db: Session, company: str | None = None, status: str | None = None) -> List[JobResponse]:
    jobs = job_repository.filter_jobs(db, company, status)
    if not jobs:
        raise HTTPException(status_code=404, detail="No jobs found for the specified filters")

    return [
        JobResponse.model_validate(job)
        for job in jobs
    ]

def filter_my_jobs(db: Session, user_id: int, company: str | None = None, status: str | None = None) -> list[JobResponse]:
    jobs = job_repository.filter_my_jobs(db, user_id, company, status)
    if not jobs:
        raise HTTPException(status_code=404, detail="No jobs found for the specified filters")

    return [
        JobResponse.model_validate(job)
        for job in jobs
    ]