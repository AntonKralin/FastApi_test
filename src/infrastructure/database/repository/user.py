from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.infrastructure.database.repository.base import BaseRepository
from src.infrastructure.database.models.user import User
from src.controllers.model.user import UserPostSchema


class UserRepository(BaseRepository[User, UserPostSchema]):

    async def get_by_username(self, username: str) -> Optional[User]:
        """Получение User по username"""
        query = select(self.model).where(self.model.username == username)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()
