# app/models/schema/persona.py

from pydantic import BaseModel


# se crea el Schema (el tipo de dato) para un vehiculo
class AuthBase(BaseModel):
    username: str
    password: str
    email: str


class AuthCreate(AuthBase):
    pass


class AuthenticateUser(BaseModel):
    username: str
    password: str


class AuthResponseToken(BaseModel):
    token: str


class AuthResponse(AuthBase):
    id: int

    class Config:
        orm_mode = True
