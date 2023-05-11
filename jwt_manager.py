from dotenv import load_dotenv
from jwt import encode
import os

load_dotenv()

key = os.getenv("JWT_KEY")


def create_token(payload: dict) -> str:
    token: str = encode(payload, key, algorithm="HS256")
    return token
