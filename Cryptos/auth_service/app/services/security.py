from argon2 import (PasswordHasher,
                    exceptions)

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
