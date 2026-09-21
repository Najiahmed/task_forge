from database.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(100), index=True)
    completed: Mapped[bool] = mapped_column(default=False)