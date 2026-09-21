from pydantic import BaseModel, Field, ConfigDict


class TaskCreate(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    completed: bool = False


class TaskUpdate(BaseModel):
    title: str | None = Field(
        default=None,
        min_length=3,
        max_length=100,
    )
    completed: bool | None = None


class TaskResponse(BaseModel):
    #from_attributes=True signifie Pydantic peut construire la réponse depuis les attributs d'un objet Python/ORM.
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    completed: bool
