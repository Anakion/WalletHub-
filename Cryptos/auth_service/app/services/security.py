from datetime import timedelta, datetime

import jwt
from argon2 import (PasswordHasher,
                    exceptions)

from Cryptos.auth_service.app.core.config import settings

hasher = PasswordHasher()


def hash_password(password: str) -> str:
    """
        Hashes the password using Argon2.

        :param password: Password to hash.
        :return: The hashed password as a string.
    """
    return hasher.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    """
        Verifies if the provided password matches the hashed password.

        :param password: Password to verify.
        :param hashed_password: Hashed password to compare with.
        :return: True if the password matches the hashed password, False otherwise.
    """
    try:
        return hasher.verify(hashed_password, password)
    except exceptions.VerifyMismatchError:
        return False


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=5)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def decode_jwt_token(encoded_token: str):
    try:
        decoded = jwt.decode(encoded_token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return decoded
    except jwt.ExpiredSignatureError:
        return Exception("Token has expired")
    except jwt.InvalidTokenError:
        return Exception("Invalid token")

