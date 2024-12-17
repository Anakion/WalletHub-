from sqlalchemy import (Integer,
                        String)
from sqlalchemy.orm import (Mapped,
                            mapped_column)

from Cryptos.auth_service.app.db.base import Base


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    email: Mapped[str] = mapped_column(String, unique=True)
    password: Mapped[str] = mapped_column(String, nullable=False)

