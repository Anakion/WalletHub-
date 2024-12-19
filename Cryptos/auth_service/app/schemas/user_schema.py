from pydantic import BaseModel, EmailStr


class RegisterUser(BaseModel):
    username: str
    email: EmailStr
    password: str


class LoginUser(BaseModel):
    email: str
    password: str
