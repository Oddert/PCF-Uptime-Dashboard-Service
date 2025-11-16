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
