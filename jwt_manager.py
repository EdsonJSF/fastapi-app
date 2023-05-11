from dotenv import load_dotenv
from jwt import encode
import os

load_dotenv()

jwt_key = os.getenv("JWT_KEY")


def create_token(data: dict):
    token: str = encode(payLoad=data, key=jwt_key, algorithm="HS256")
