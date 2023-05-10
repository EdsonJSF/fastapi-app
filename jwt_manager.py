from jwt import encode


def create_token(data: dict):
    token: str = encode(payLoad=data, key="my_secret_key", algorithm="HS256")
