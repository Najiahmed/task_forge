from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from database.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    completed: Mapped[bool] = mapped_column(default=False)

    priority: Mapped[Optional[int]] = mapped_column(
        nullable=True
        )

    meta_data: Mapped[Optional[str]] = mapped_column(
        nullable=True
    )

class Member(Base):
    __tablename__ = "members"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    is_active: Mapped[bool] = mapped_column(default=True)
    