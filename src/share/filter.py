from enum import Enum
from pydantic import BaseModel


class FilterOptions(str, Enum):
    EQ = 'eq'
    NE = 'ne'
    GT = 'gt'
    GE = 'ge'
    LT = 'lt'
    LE = 'le'
    LIKE = 'like'
    ILIKE = 'ilike'
    IN = 'in'
    NOT_IN = 'not_in'
    NULL = 'null'
    NOT_NULL = 'not_null'


class FilterField(BaseModel):
    