from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.annotation import Annotated

from Cryptos.auth_service.app.db.session import get_async_session
from Cryptos.auth_service.app.schemas.user_schema import RegisterUser

router = APIRouter(
    prefix="/api/v1/users",
    tags=["Users"]
)


@router.post("/register")
async def register(db:  Annotated[AsyncSession, Depends(get_async_session)],
                   register_data: RegisterUser):
    pass
