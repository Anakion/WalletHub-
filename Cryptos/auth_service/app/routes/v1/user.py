from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.annotation import Annotated

from Cryptos.auth_service.app.db.session import get_async_session
from Cryptos.auth_service.app.schemas.user_schema import RegisterUser
from Cryptos.auth_service.app.services.user_service import create_user

router = APIRouter(
    prefix="/api/v1/users",
    tags=["Users"]
)


@router.post("/register")
async def register(register_data: RegisterUser, db: AsyncSession = Depends(get_async_session)):
    return await create_user(db, register_data)


