
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer

from helpers.jwt_manager import validate_token


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data['email'] != "string":
            raise HTTPException(
                status_code=403, detail="Credenciales invalidas")
