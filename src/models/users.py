from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship
from src.models.base import Base

from typing import List
class User(Base):
    __tablename__ = 'users'

    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(String(50), nullable=False)
    lastname:Mapped[str] = mapped_column(String(50), nullable=False)
    password:Mapped[str] = mapped_column(String(50), nullable=False)
    
    student_id:Mapped[List["Student"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )

    def __init__(self, name: str,lastname:str, password: str):
        self.name = name
        self.lastname = lastname
        self.password = password    

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, lastname={self.lastname}, password={self.password})"