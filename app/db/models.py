from datetime import datetime
from enum import StrEnum, auto

from sqlalchemy import Enum, ForeignKey, String, func

from app.db.database import Base
from sqlalchemy.orm import Mapped, mapped_column

class JobStatus(StrEnum):
    APPLIED = auto()
    INTERVIEWING = auto()
    OFFERED = auto()
    REJECTED = auto()


class Job(Base):
    __tablename__ = "job"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(128), nullable=False)
    company: Mapped[str] = mapped_column(String(128), nullable=False, index=True)
    status: Mapped[JobStatus] = mapped_column(
    String(32),
    nullable=False,
    index=True
)
    created_at: Mapped[datetime] = mapped_column(server_default=func.current_timestamp())
    updated_at: Mapped[datetime] = mapped_column(onupdate=func.current_timestamp(), server_default=func.current_timestamp(), nullable=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

    def __repr__(self):
        return f"<Job(id={self.id}, title={self.title!r}, company={self.company!r}, status={self.status.value})>"

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(128), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(128), nullable=False)