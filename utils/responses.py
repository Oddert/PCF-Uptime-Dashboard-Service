"""Collection of standard response formatters to enforce consistency across all endpoints and enable cleaner code."""

from fastapi import Response, status as http_statuses


def respond_ok(
    response: Response | None = None,
    message: str = 'Request processed successfully.',
    status: int = 200,
    error: str | None = None,
    **kwargs,
):
    """Handless 200 code "OK" responses."""
    if response:
        response.status_code = http_statuses.HTTP_200_OK
    return {
        'status': status,
        'message': message,
        'error': error,
        **kwargs,
    }

def respond_not_found(
    response: Response | None = None,
    message: str = 'The requested resource could not be found. Please check the request and try again.',
    status: int = 404,
    error: str | None = 'Not found.',
    **kwargs,
):
    """Handless 404 "Not found" responses."""
    if response:
        response.status_code = http_statuses.HTTP_404_NOT_FOUND
    return {
        'status': status,
        'message': message,
        'error': error,
        **kwargs,
    }

def respond_server_error(
    response: Response | None = None,
    message: str = 'Something went wrong processing your request.',
    status: int = 500,
    error: str | None = 'Unknown server error.',
    **kwargs,
):
    """Handless generic 500 band responses for non-elaborated server errors."""
    if response:
        response.status_code = http_statuses.HTTP_500_INTERNAL_SERVER_ERROR
    return {
        'status': status,
        'message': message,
        'error': error,
        **kwargs,
    }
