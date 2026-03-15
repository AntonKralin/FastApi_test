from datetime import datetime, UTC

from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class TimestampMixin:
    created_at = Column(DateTime, nullable=False, default=datetime.now(UTC))
    updated_at = Column(DateTime, nullable=False, default=datetime.now(UTC),
                        onupdate=datetime.now(UTC))


class BaseModel(Base, TimestampMixin):
    __abstract__ = True

    id = Column(Integer, primary_key=True)


class BaseModelOnlyId(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
