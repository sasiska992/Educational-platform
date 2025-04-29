from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship
from src.models.base import Base

from typing import List


class HashedPassword:
    from passlib.context import CryptContext

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    def hash(cls, password: str):  # Изменено на cls
        print(cls.pwd_context.hash(password))
        return cls.pwd_context.hash(password)

    @classmethod
    def verify(cls, password: str, hashed_password: str) -> bool:  # Изменено на cls
        return cls.pwd_context.verify(password, hashed_password)


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    lastname: Mapped[str] = mapped_column(String(50), nullable=False)
    password: Mapped[str] = mapped_column(String(128), nullable=False)
    role: Mapped[str] = mapped_column(String(50), nullable=False)

    # Связи
    teacher: Mapped["Teacher"] = relationship(
        "Teacher", back_populates="user", uselist=False
    )
    student: Mapped["Student"] = relationship(
        "Student", back_populates="user", uselist=False
    )

    def __init__(self, name: str, lastname: str, password: str, role: str = "student"):
        self.name = name
        self.lastname = lastname
        self.password = HashedPassword.hash(password)
        self.role = role

    def check_password(self, password: str):
        return HashedPassword.verify(password, self.password)

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, lastname={self.lastname}, password={self.password})"
