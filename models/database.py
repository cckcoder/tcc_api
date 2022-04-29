from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from decouple import config

DEBUG = config("DEBUG", default=False, cast=bool)


if DEBUG:
    SQLALCHEMY_DATABASE_URL = "sqlite:///./tcc_inventory.db"
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
else:
    DATABASE_URL = config("DATABASE_URL")
    engine = create_engine(DATABASE_URL)


session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    try:
        db = session_local()
        yield db
    finally:
        db.close()
