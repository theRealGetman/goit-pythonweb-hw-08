from sqlalchemy import Integer, String, Date
from sqlalchemy.orm import Mapped, mapped_column

from datetime import date as d

from src.db.models.base import Base


class Contact(Base):
    __tablename__ = "contacts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    phone: Mapped[str] = mapped_column(String(15))
    email: Mapped[str] = mapped_column(String(50))
    date_of_birth: Mapped[d] = mapped_column(Date)
