from fastapi import APIRouter

from helpers.jwt_manager import create_token
from schemas.auth import User

auth_router = APIRouter()


@auth_router.post('/auth', tags=['auth'])
def create_user(user: User):
    if user.email == "string" and "string":
        token: str = create_token(user.dict())
    return token
