# MecanicaMs/app/crud/auth.py
import uuid
from typing import Optional

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.services.auth_service import hash_password, is_the_same_password
from app.models.domain.auth import AuthUser
from app.models.schema.auth import AuthCreate, AuthResponseToken, AuthenticateUser


def create_auth_user(db: Session, usuario: AuthCreate) -> Optional[AuthResponseToken]:
    auth_token = str(uuid.uuid4())
    hashed_password = hash_password(usuario.password)
    auth_user_db = AuthUser(
        username=usuario.username,
        password=hashed_password,
        email=usuario.email,
        token=auth_token
    )
    print(auth_user_db)
    try:
        db.add(auth_user_db)
        db.commit()
        return AuthResponseToken(token=auth_token)
    except IntegrityError as ie:
        db.rollback()
        return None


def auth_user(db: Session, user: AuthenticateUser) -> Optional[AuthResponseToken]:
    authenticated_user = db.query(AuthUser).filter(AuthUser.username == user.username).first()
    if not authenticated_user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    if not is_the_same_password(password=user.password, auth_password=authenticated_user.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return AuthResponseToken(token=authenticated_user.token)
