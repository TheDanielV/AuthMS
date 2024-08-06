# app/services/auth_service.py
import base64
import hashlib
import os

from dotenv import load_dotenv

load_dotenv()  # Cargar variables desde .env


def get_salt():
    return base64.b64decode(os.getenv("SALT"))


def hash_password(password):
    n = 2 ** 14
    r = 8
    p = 1
    maxmem = 0
    dklen = 64
    hashed_password = hashlib.scrypt(password.encode(), salt=get_salt(), n=n, r=r, p=p, maxmem=maxmem, dklen=dklen)
    print(get_salt())
    return hashed_password.hex()


def is_the_same_password(password, auth_password):
    if auth_password == hash_password(password):
        return True
    else:
        return False
