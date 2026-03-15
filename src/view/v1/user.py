from fastapi import APIRouter, Depends

from schema.user import UserGetSchema
from repository.user import UserData
from model.user import User
from settings.database import get_session


router = APIRouter(prefix="/users", tags=["Users"])


@router.get('/', response_model=list[UserGetSchema] | None)
async def get_users(session=Depends(get_session)):
    try:
        user_model = UserData(User, session)
        users = await user_model.get_multi()
        return [UserGetSchema.from_orm(user) for user in users]
    except Exception as e:
        print(e)
        return None
