import os
import uuid
from datetime import datetime, timedelta, timezone

import jwt
from passlib.context import CryptContext

SECRET_KEY = os.getenv("JWT_SECRET_KEY", "secret_by_alfialdo_for_local_dev")
TOKEN_EXPIRED_MINUTE = 60 * 24 * 3  # 3 days
HASH_ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def create_access_token(subject: uuid.UUID) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=TOKEN_EXPIRED_MINUTE)
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=HASH_ALGORITHM)
    return encoded_jwt
