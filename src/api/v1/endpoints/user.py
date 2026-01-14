from typing import List

from fastapi import APIRouter, Depends, Query

from src.controllers.ser


router = APIRouter(prefix="/users", tags=["users"])

@router.get('/', response_model=List[User])