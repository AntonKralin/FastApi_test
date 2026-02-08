from datetime import datetime

from pydantic import BaseModel


class UserBaseSchema(BaseModel):
    username: str
    password: str
    is_active: bool


class UserGetSchema(UserBaseSchema):
    id: int
    created_at: datetime
    updated_at: datetime
