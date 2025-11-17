"""Handles all responses on the base endpoint "/"."""

from fastapi import APIRouter, Depends, Request, Response
from sqlalchemy.orm import Session

from config.database import get_db

from models.user_model import UserModel

from schemas.auth_schemas import PostLogin, PostSignup

from security.hash import get_hashed_pwd, verify_hashed_pwd
from security.token import create_access_jwt, create_refresh_jwt

from utils.responses import (
    respond_bad_request,
    respond_ok,
    respond_server_error,
    respond_unauthenticated,
)

router = APIRouter(prefix='/auth')


@router.post('/signup')
def create_user(
    request: Request,
    response: Response,
    user: PostSignup,
    database: Session = Depends(get_db),
):
    """Fallback endpoint for the root of the API."""

    try:
        # IDEA: Potentially add additional final password validation.
        retrieved_user = UserModel.find_by_username(user.username, database)

        if retrieved_user:
            return respond_bad_request(
                response, message='A user with that username already exists.'
            )

        created_user = UserModel(
            areas=','.join(user.areas),
            password=get_hashed_pwd(user.password),
            readable_name=user.readableName if user.readableName else user.username,
            username=user.username,
        )

        database.add(created_user)
        database.commit()
        database.flush()

        return respond_ok(response, user=created_user.to_json())
    except Exception as ex:
        return respond_server_error(response, error=str(ex))


@router.post('/login')
def login_user(
    request: Request,
    response: Response,
    user: PostLogin,
    database: Session = Depends(get_db),
):
    """Fallback endpoint for the root of the API."""

    try:
        retrieved_user = UserModel.find_by_username(user.username, database)

        if not retrieved_user:
            return respond_bad_request(
                response, message='No user by that username exists.'
            )

        if not verify_hashed_pwd(user.password, bytes.fromhex(retrieved_user.password)):  # type: ignore
            return respond_unauthenticated(
                response, message='Incorrect username or password.'
            )

        access_token = create_access_jwt(
            retrieved_user.username, retrieved_user.get_roles_as_list() # type: ignore
        )
        refresh_token = create_refresh_jwt(retrieved_user.username) # type: ignore

        return respond_ok(
            response, accessToken=access_token, refreshToken=refresh_token
        )
    except Exception as ex:
        return respond_server_error(response, error=str(ex))
