from pydantic import BaseModel, Field, ConfigDict

class UserCreate(BaseModel):
    email: str 
    password: str = Field(min_length=8, max_length=128)

class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: str
    is_active: bool