from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.infrastructure.database.repository.base import BaseRepository
from src.infrastructure.database.models.user import User
from src.controllers.model.user import UserPostSchema


class UserRepository(BaseRepository[User, UserPostSchema]):
    pass
