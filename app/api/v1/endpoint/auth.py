from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.auth_service import get_salt
from app.models.schema.auth import *
from app.crud.auth import *
from app.db.session import get_db

router = APIRouter()


@router.post("/", response_model=AuthResponseToken)
def create_new_user(user: AuthCreate, db: Session = Depends(get_db)):
    result = create_auth_user(db, user)
    if result is None:
        raise HTTPException(status_code=422, detail="El usuario ya existe")
    else:
        return result


@router.post("/authenticate", response_model=AuthResponseToken)
def create_new_user(user: AuthenticateUser, db: Session = Depends(get_db)):
    result = auth_user(db, user)
    return result
