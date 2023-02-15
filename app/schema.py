from pydantic import BaseModel
from app.utils import get_hashed_password


class TokenPayload(BaseModel):
    sub: str = None
    exp: int = None


class UserOut(BaseModel):
    email: str


class SystemUser(UserOut):
    password: str


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str

    class Config:
        orm_mode = True


class User(BaseModel):
    username: str
    email: str
    age: int
    password: str

    class Config:
        orm_mode = True


