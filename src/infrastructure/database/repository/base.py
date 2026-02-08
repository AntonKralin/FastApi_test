from typing import Generic, TypeVar, Type, Optional, List, Dict, Any

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from pydantic import BaseModel


ModelType = TypeVar("ModelType")
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class BaseRepository(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType], session: AsyncSession):
        self.model = model
        self.session = session

    async def create(self, obj_in: CreateSchemaType) -> ModelType:
        try:
            db_obj = self.model(**obj_in.model_dump())
            self.session.add(db_obj)
            await self.session.commit()
            await self.session.refresh(db_obj)
            return db_obj
        except Exception as e:
            await self.session.rollback()
            raise e

    async def get_one(self, id: int) -> Optional[ModelType]:
        """Получение по id"""
        stmt = select(self.model).where(self.model.id == id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def get_multi(
        self,
        skip: int = 0,
        limit: int = 100,
        filters: Optional[Dict[str, Any]] = None,
        order_by: Optional[List] = None,
    ) -> List[ModelType]:
        """Получение списка с пагинацией"""
        query = select(self.model).offset(skip).limit(limit)
        if filters:
            for filter in filters:
                if hasattr(self.model, filter):
                    query = query.where(
                        getattr(self.model, filter) == filters[filter])
        if order_by:
            query = query.order_by(*order_by)
        else:
            query = query.order_by(self.model.id)

        result = await self.session.execute(query)
        return result.scalars().all()

    async def update_by_id(
            self, id: int, obj_in: UpdateSchemaType) -> ModelType:
        """Обновление по id"""
        db_obj = await self.get(id)
        if not db_obj:
            return None
        for field, value in obj_in.model_dump(exclude_unset=True).items():
            setattr(db_obj, field, value)
        self.session.add(db_obj)
        await self.session.commit()
        await self.session.refresh(db_obj)
        return db_obj

    async def delete(self, id: int) -> bool:
        """Удаление по id"""
        db_obj = await self.get(id)
        if not db_obj:
            return False
        await self.session.delete(db_obj)
        await self.session.commit()
        return True
