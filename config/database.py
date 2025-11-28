from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = (
    'postgresql+psycopg2://postgres:mysecretpassword@host.docker.internal:5432/postgres'
)

engine = create_engine(DATABASE_URL)

ORMBase = declarative_base()

SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
