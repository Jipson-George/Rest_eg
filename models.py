
from sqlalchemy import String, types, ForeignKey, func, Boolean, PrimaryKeyConstraint
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



class Base (DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class Country(db.Model):
    __tablename__ = "countries"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    iso: Mapped[str] = mapped_column(String(4), nullable=False, unique=True)
    isd: Mapped[str] = mapped_column(String(4), nullable=False, unique=True)
    languageCode: Mapped[str] = mapped_column(String(10), nullable=False)
    language: Mapped[str] = mapped_column(String(50), nullable=False)
    currencyCode: Mapped[str] = mapped_column(String(10), nullable=False)
    currencySymbol: Mapped[str] = mapped_column(String(10), nullable=False)
    minimumAge: Mapped[int] = mapped_column(nullable=True)
