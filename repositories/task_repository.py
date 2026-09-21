from sqlalchemy.orm import Session
from models.tasks import Task
from sqlalchemy import select



def get_all_tasks(db:Session,completed: bool | None = None):
    if completed is None:
        tasks = db.scalars(select(Task)).all()
        return tasks

    tasks = db.scalars(select(Task).where(Task.completed == completed)).all()
    return tasks
    


def get_task_by_id(db: Session, task_id: int):
    task = db.scalars(select(Task).where(Task.id == task_id)).first()
    return task


def create_task(db: Session, task_data: dict):
    new_task = Task(**task_data)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


def update_task(db: Session, existing_task: Task, update_data: dict):
    for key, value in update_data.items():
        setattr(existing_task, key, value)
    db.commit()
    db.refresh(existing_task)
    return existing_task


def delete_task(db: Session, existing_task: Task):
    db.delete(existing_task)
    db.commit()
