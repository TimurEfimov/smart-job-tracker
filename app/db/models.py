from datetime import datetime
import enum

from sqlalchemy import Enum, ForeignKey, String, func

from app.db.database import Base
from sqlalchemy.orm import Mapped, mapped_column

class JobStatus(enum.Enum):
    APPLIED = "applied"
    INTERVIEWING = "interviewing"
    OFFERED = "offered"
    REJECTED = "rejected"


class Job(Base):
    __tablename__ = "job"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(128), nullable=False)
    company: Mapped[str] = mapped_column(String(128), nullable=False, index=True)
    status: Mapped[JobStatus] = mapped_column(
        Enum(JobStatus, values_callable=lambda x: [e.value for e in x]), 
        nullable=False, 
        index=True
    )
    created_at: Mapped[datetime] = mapped_column(server_default=func.current_timestamp())
    updated_at: Mapped[datetime] = mapped_column(onupdate=func.current_timestamp(), server_default=func.current_timestamp(), nullable=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)

def __repr__(self):
    return f"<Job(id={self.id}, title={self.title!r}, company={self.company!r}, status={self.status.value})>"

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(128), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(128), nullable=False)