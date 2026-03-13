from fastapi import APIRouter, HTTPException
from jose import jwt
from datetime import datetime, timedelta

router = APIRouter()

SECRET_KEY = "erp_secret_key"
ALGORITHM = "HS256"
TOKEN_EXPIRE_MINUTES = 60


@router.post("/login")
def login(username: str, password: str):

    # Simple demo authentication
    if username != "admin" or password != "admin":
        raise HTTPException(status_code=401, detail="Invalid credentials")

    payload = {
        "sub": username,
        "exp": datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRE_MINUTES)
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    return {
        "access_token": token,
        "token_type": "bearer"
    }
