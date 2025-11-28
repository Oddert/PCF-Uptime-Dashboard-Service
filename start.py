"""Entry point for the application."""

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from uvicorn import run

from resources import auth_resources, instance_resources, root_resources

from utils.schedulers import setup_async_schedulers


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan handler for the application, initialising jobs on startup."""
    # Initialise schedulers on app load.
    async_schedulers = setup_async_schedulers()
    app.state.scheduler = async_schedulers
    if async_schedulers:
        async_schedulers.start()
        logger.info(f'Schedulers started: {async_schedulers}')
    yield
    # Deactivate the app schedulers on app shutdown.
    scheduler: AsyncIOScheduler | None = app.state.scheduler
    if scheduler:
        scheduler.shutdown()


app = FastAPI(lifespan=lifespan)

allowed_origins = [
    'http://localhost:8080',
    'http://localhost:5173',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

routes = [
    (auth_resources.router, 'Auth'),
    (instance_resources.router, 'Instances'),
    (root_resources.router, 'Root'),
]

for route, tags in routes:
    logger.info(f'Initialising route: {tags}')
    app.include_router(route, prefix='/api/v0', tags=[tags])


if __name__ == '__main__':
    run(
        'start:app',
        port=8080,
        reload=True,
    )
