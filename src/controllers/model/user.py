from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    username = str
    password = str
    is_active = bool


class UserGetSchema(UserBase):
    id = int
    created_at = datetime
    updated_at = datetime

    class Config:
        orm_mode = True


class UserPostSchema(UserBase):
    class Config:
        orm_mode = True
