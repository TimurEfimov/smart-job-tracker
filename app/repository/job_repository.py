from typing import List

from sqlalchemy.orm import Session

from app.db.models import Job, JobStatus

def is_job_exists(db: Session, user_id: int, job_id: int) -> bool:
    return db.query(Job).filter(Job.id == job_id, Job.user_id == user_id).first() is not None

def get_job_by_id(db: Session, user_id: int, job_id: int) -> Job | None:
    return db.query(Job).filter(Job.id == job_id, Job.user_id == user_id).first()

def create_job(db: Session, user_id: int, title: str, company: str, status: JobStatus) -> Job:
    job = Job(title=title, company=company, status=status, user_id=user_id)
    db.add(job)
    db.flush()
    return job

def delete_job(db: Session, user_id: int, job_id: int) -> None:
    job = db.query(Job).filter(Job.id == job_id, Job.user_id == user_id).first()
    if job:
        db.delete(job)

def filter_jobs(db: Session, company: str | None = None, status: str | None = None) -> List[Job]:
    query = db.query(Job)

    if company is not None:
        query = query.filter(Job.company.ilike(f"%{company}%"))

    if status is not None:
        query = query.filter(Job.status == status)

    jobs = query.all()
    return jobs

def filter_my_jobs(db: Session, user_id: int, company: str | None = None, status: str | None = None) -> List[Job]:
    query = db.query(Job).filter(Job.user_id == user_id)

    if company is not None:
        query = query.filter(Job.company.ilike(f"%{company}%"))

    if status is not None:
        query = query.filter(Job.status == status)

    jobs = query.all()
    return jobs

def update_status_job(db: Session, user_id: int, job_id: int, status: JobStatus) -> Job | None:
    job = db.query(Job).filter(Job.id == job_id, Job.user_id == user_id).first()
    if job:
        job.status = status
        db.flush()
    return job

# def delete_all_jobs(db: Session, user_id: int) -> None:
#     db.query(Job).filter(Job.user_id == user_id).delete()