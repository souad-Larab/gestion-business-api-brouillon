""" Classe de base à tous les modeles SQLAlchemy"""

from datetime import datetime, timezone

from sqlalchemy import DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

def utc_now()-> datetime:
    return datetime.now(timezone.utc)


class Base(DeclarativeBase):
    pass


class TimestampMixin:
    """ utilisée pour l'ajout des colonnes: cree_le et modifie_le à une table """

    cree_le: Mapped[datetime]= mapped_column(
        DateTime(timezone= True), default= utc_now
        )

    modifie_le: Mapped[datetime]= mapped_column(
        DateTime(timezone= True), default= utc_now, onupdate= utc_now
    )

    