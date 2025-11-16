"""Entry point for the application."""

from fastapi import FastAPI
from loguru import logger
from uvicorn import run

from resources import root_resources

app = FastAPI()

routes = [(root_resources.router, 'Root')]

for route, tags in routes:
    logger.info(f'Initialising route: {tags}')
    app.include_router(route, prefix='/api/v0', tags=[tags])

if __name__ == '__main__':
    run(
        'start:app',
        port=8080,
        reload=True,
    )
