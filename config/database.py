from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from config.variables import PG_USERNAME, PG_PASSWORD, PG_HOST, PG_PORT, PG_DATABASE

DATABASE_URL = f'postgresql+psycopg2://{PG_USERNAME}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DATABASE}'

engine = create_engine(DATABASE_URL, connect_args={'ssl_ca': './global-bundle.pem'})

ORMBase = declarative_base()

SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
