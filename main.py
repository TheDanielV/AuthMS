from fastapi import FastAPI
from app.api.v1.endpoint import auth
from app.db.init_db import init_db

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])


@app.on_event("startup")
def on_startup():
    init_db()
