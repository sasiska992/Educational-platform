from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship
from src.models.base import Base


class Homework(Base):
    __tablename__ = "homeworks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(50), nullable=False)
    lesson_id: Mapped[int] = mapped_column(ForeignKey("lessons.id"), nullable=False)

    lesson: Mapped["Lesson"] = relationship("Lesson", back_populates="homework")

    def __init__(self, name: str, description: str, lesson_id: int):
        self.name = name
        self.description = description
        self.lesson_id = lesson_id

    def __repr__(self):
        return (
            f"Homework(id={self.id}, name={self.name}, description={self.description})"
        )
