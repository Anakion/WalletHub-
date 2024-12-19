from typing import Dict

from asyncpg.pgproto.pgproto import timedelta
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from Cryptos.auth_service.app.core.config import settings
from Cryptos.auth_service.app.models import User
from Cryptos.auth_service.app.schemas.user_schema import RegisterUser, LoginUser
from Cryptos.auth_service.app.services.security import hash_password, create_access_token, verify_password


async def create_user(db: AsyncSession, user: RegisterUser) -> Dict[str, str]:
    result = await db.execute(select(User).filter(User.email == user.email))
    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Email already registered")

    hashed_password = hash_password(user.password)

    db_user = User(username=user.username, email=user.email, password=hashed_password)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)

    # Generation JWT token

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}


async def check_user_in_database(db: AsyncSession, email: str) -> User | None:
    result = await db.execute(select(User).filter(User.email == email))
    existing_user = result.scalar_one_or_none()
    if not existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="User not found")
    return existing_user


async def authenticate_user(db: AsyncSession, data: LoginUser) -> Dict[str, str]:
    user = await check_user_in_database(db, data.email)

    if not verify_password(data.password, str(user.password)):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid credentials")

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}