from fastapi import APIRouter
from pydantic import BaseModel

from helpers.jwt_manager import create_token

auth_router = APIRouter()


class User(BaseModel):
    email: str
    password: str


@auth_router.post('/auth', tags=['auth'])
def create_user(user: User):
    if user.email == "string" and "string":
        token: str = create_token(user.dict())
    return token
