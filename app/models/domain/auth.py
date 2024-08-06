# app/models/domain/persona.py

from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.database import Base


# Se crea el modelo paara un usuario
class AuthUser(Base):
    __tablename__ = "auth"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(225), index=True, unique=True  )
    password = Column(String(225), index=True)
    email = Column(String(225), index=True, unique=True)
    token = Column(String(225), index=True, unique=True)



