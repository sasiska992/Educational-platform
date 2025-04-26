from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, foreign
from sqlalchemy.orm import mapped_column, relationship
from src.models.base import Base

class Student(Base):
    __tablename__ = 'students'

    id:Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[int] = mapped_column(ForeignKey('users.id'), unique=True, nullable=False)

    user:Mapped["User"] = relationship(back_populates="student_id")

    
    def __init__(self, user_id: int):
        self.user_id = user_id

    def __repr__(self):
        return f"Student(id={self.id}, user_id={self.user_id})"