from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from src.core.database import get_db
from src.core.security import TOKEN_EXPIRED_MINUTE, create_access_token
from src.features.auth import schemas, service
from src.features.auth.dependencies import get_current_user
from src.features.auth.models import User

auth_router = APIRouter(prefix="/api/auth", tags=["Authentication"])
user_router = APIRouter(prefix="/api", tags=["User"])


@auth_router.post("/signup", response_model=schemas.UserResponse)
def signup(user_in: schemas.UserSignUp, db: Session = Depends(get_db)):
    return service.create_user(db=db, user_in=user_in)


@auth_router.post("/signin")
def signin(
    user_in: schemas.UserLogin, response: Response, db: Session = Depends(get_db)
):
    user = service.authenticate_user(db, user_in.email, user_in.password)
    access_token = create_access_token(subject=user.id)

    # Include the HttpOnly Cookie
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        max_age=60 * TOKEN_EXPIRED_MINUTE,  # in seconds
        samesite="lax",
        secure=False,
    )
    return {"message": "Successfully logged in"}


@auth_router.post("/signout")
def signout(response: Response):
    response.delete_cookie(key="access_token", httponly=True, samesite="lax")
    return {"message": "Successfully logged out"}


@user_router.get("/me")
def get_current_user_profile(current_user: User = Depends(get_current_user)):
    username = current_user.email.split("@")[0]
    return {"message": f"Welcome, {username}"}
