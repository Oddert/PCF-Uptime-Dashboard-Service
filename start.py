from fastapi import FastAPI
from loguru import logger
from uvicorn import run

from resources import root_resources

app = FastAPI()

routes = [(root_resources.router, 'Root')]

for route in routes:
    logger.log(f'Initialising route collection: {route[1]}')
    app.add_route(route[0])

if __name__ == '__main__':
    run(
        'start:app',
        port=8080,
        reload=True,
    )
