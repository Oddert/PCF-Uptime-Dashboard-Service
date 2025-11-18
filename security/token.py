"""Functions to create and validate user access tokens and refresh tokens."""

import jwt

from datetime import datetime, timedelta
from uuid import uuid4 as uuid
from typing import List, Any


jwt_access_secret = '123456789'
jwt_refresh_secret = '123456789'
jwt_alg = 'HS256'


class JWTDecodeResult:
    def __init__(
        self,
        _error: str | None = None,
        _success: bool = False,
        _payload: Any = None,
    ) -> None:
        self.success = _success
        self.payload = _payload
        self.error = _error


def create_access_jwt(username: str, roles: List[str]):
    """Creates a user Access Token."""
    token_body = {
        'sub': username,
        'jti': str(uuid()),
        'roles': roles,
        'exp': datetime.now() + timedelta(hours=1),
    }
    return jwt.encode(token_body, jwt_access_secret, algorithm=jwt_alg)


def create_refresh_jwt(username: str):
    """Creates a user Refresh Token."""
    token_body = {
        'sub': username,
        'jti': str(uuid()),
        'exp': datetime.now() + timedelta(days=3),
    }
    return jwt.encode(token_body, jwt_refresh_secret, algorithm=jwt_alg)


def validate_and_decode_jwt(token: str, secret: str) -> JWTDecodeResult:
    """Validates a JWT for a given secret."""
    try:
        payload = jwt.decode(token, secret, algorithms=[jwt_alg])
        return JWTDecodeResult(None, True, payload)
    except jwt.ExpiredSignatureError:
        return JWTDecodeResult('Token has expired.')
    except jwt.InvalidTokenError:
        return JWTDecodeResult('Token is invalid.')
    except Exception as ex:
        return JWTDecodeResult(str(ex))


def validate_access_jwt(access_token: str) -> JWTDecodeResult:
    """Decodes and validates a user's access token."""
    return validate_and_decode_jwt(access_token, jwt_access_secret)


def validate_refresh_jwt(refresh_token: str) -> JWTDecodeResult:
    """Decodes and validates a user's refresh token."""
    return validate_and_decode_jwt(refresh_token, jwt_access_secret)
