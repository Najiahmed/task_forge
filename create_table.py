import database.database
from models.tasks import Task

database.database.Base.metadata.create_all(bind=database.database.engine)