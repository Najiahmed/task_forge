from schemas.tasks import TaskCreate, TaskUpdate
from sqlalchemy.orm import Session
import repositories.task_repository as task_repository


def get_all_tasks(db: Session, completed: bool | None = None):
    return task_repository.get_all_tasks(db, completed)


def get_task_by_id(db: Session, task_id: int):
    return task_repository.get_task_by_id(db, task_id)


def create_task(db: Session, task: TaskCreate):
    task_data = task.model_dump()
    return task_repository.create_task(db, task_data)


def update_task(db: Session, task_id: int, task_update: TaskUpdate):
    existing_task = task_repository.get_task_by_id(db, task_id)

    if existing_task is None:
        return None

    update_data = task_update.model_dump(
        exclude_unset=True,
        exclude_none=True,
    )

    return task_repository.update_task(
        db,
        existing_task,
        update_data,
    )


def delete_task(db: Session, task_id: int):
    existing_task = task_repository.get_task_by_id(db, task_id)

    if existing_task is None:
        return False

    task_repository.delete_task(db, existing_task)
    return True
