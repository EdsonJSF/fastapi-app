from dotenv import load_dotenv
from jwt import encode, decode
import os

load_dotenv()

key = os.getenv("JWT_KEY")


def create_token(payload: dict) -> str:
    token: str = encode(payload, key, algorithm="HS256")
    return token


def validate_token(token: str) -> dict:
    token = decode(token, key, algorithms=['HS256'])
    return token
