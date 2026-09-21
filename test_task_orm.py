from database.database import SessionLocal
from models.tasks import Task
from sqlalchemy import select

db = SessionLocal()

try:

    # Example usage
    new_task = Task(title="Learn SQLAlchemy", completed=False)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    print(new_task.id)

    tasks = db.scalars(select(Task)).all()
    for task in tasks:
        print(task.id, task.title, task.completed)
finally:
    db.close()