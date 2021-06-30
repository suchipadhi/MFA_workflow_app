from pydantic import BaseModel, Field


class UserList(BaseModel):
    email: str


class UserCreate(BaseModel):
    email: str = Field(..., example="test@gmail.com")
    password: str = Field(..., example="test")

