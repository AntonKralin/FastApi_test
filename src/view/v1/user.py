from fastapi import APIRouter

from schema.user import UserGetSchema


router = APIRouter(prefix="/users", tags=["Users"])


@router.get('/', response_model=UserGetSchema)
async def users():
    return []
