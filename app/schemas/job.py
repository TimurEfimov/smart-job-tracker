from pydantic import BaseModel, ConfigDict, Field, field_validator
from app.db.models import JobStatus

class JobCreateRequest(BaseModel):
    title: str = Field(..., max_length=128)
    company: str = Field(..., max_length=128)
    status: JobStatus = JobStatus.APPLIED

    @field_validator("title")
    def title_not_empty(cls, v: str) -> str:
        v = v.strip()

        if not v:
            raise ValueError("Title must not be empty")
        return v
    
    @field_validator("company")
    def company_not_empty(cls, v: str) -> str:
        v = v.strip()

        if not v:
            raise ValueError("Company must not be empty")
        return v
    
class JobResponse(JobCreateRequest):
    id: int
    model_config = ConfigDict(from_attributes=True)
