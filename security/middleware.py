from functools import wraps
from typing import List, Optional

from fastapi import Request, Response

from constants.auth_constants import role_lookup

from security.token import validate_access_jwt

from utils.exceptions import NeedsLogin, NeedsAuthorisation
from utils.responses import (
    respond_unauthenticated,
    respond_unauthorised,
    respond_server_error,
)


def protected_endpoint(for_areas: Optional[List[str]] = None):
    """
    Middleware to protect resources from access by unauthenticated of unauthorised users.
    Passing a list of area codes to
    """

    def decorator(func):
        @wraps(func)
        async def decorated(request: Request, response: Response, *args, **kwargs):
            try:
                access_token = extract_access_token(request)
                token_verify_result = validate_access_jwt(access_token)

                if not token_verify_result.success:
                    raise NeedsLogin(
                        token_verify_result.error
                        if token_verify_result.error
                        else 'Token decode failed.'
                    )

                token = token_verify_result.payload

                if 'roles' not in token:
                    raise NeedsLogin('Token format invalid.')

                access_granted = False

                for role in token['roles']:
                    if role in role_lookup:
                        if for_areas:
                            access_group = role_lookup[role]['access_codes']
                            for required_area in for_areas:
                                if required_area in access_group:
                                    access_granted = True
                        else:
                            access_granted = True

                if not access_granted:
                    raise NeedsAuthorisation(
                        'Insufficient roles for requested resource.'
                    )

                kwargs['racfid'] = token['sub']
                kwargs['roles'] = token['roles']

                return await func(request=request, response=response, *args, **kwargs)

            except NeedsLogin as ex:
                return respond_unauthenticated(
                    response=response, message=ex.message, error=ex.desc
                )
            except NeedsAuthorisation as ex:
                return respond_unauthorised(
                    response=response, message=ex.message, error=ex.desc
                )
            except Exception as ex:
                return respond_server_error(response=response, error=str(ex))

        return decorated

    return decorator


def extract_access_token(request: Request) -> str:
    """Extracts the authorisation header from an incoming request, validates the Bearer token format, and returns what is believed to be a valid token (pre-verification and decoding)."""
    auth = request.headers.get('Authorization', None)
    if not auth:
        raise NeedsLogin('No authorisation header found in request.')
    auth_segments = auth.split(' ')
    if not auth.lower().startswith('bearer ') or len(auth_segments) != 2:
        raise NeedsLogin('Header "Authorization" was not a valid Bearer token.')
    return auth_segments[1]
