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