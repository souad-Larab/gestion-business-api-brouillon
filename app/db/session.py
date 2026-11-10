""" Connexionà la BD et session par requête """

from _collections_abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import get_settings


settings = get_settings()

connect_arg = {}
if settings.database_url.startswith("sqlite"):
    connect_args = {"check_same_thread": False}

engine = create_engine(settings.database_url, connect_args= connect_args)
SessionLocal= sessionmaker(bind= engine, autoflush= False, expire_on_commit= False)



def get_bd()-> Generator[Session, None, None]:

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
