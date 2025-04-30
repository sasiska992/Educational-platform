from typing import List
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, foreign
from sqlalchemy.orm import mapped_column, relationship
from src.models.base import Base


class Lesson(Base):
    __tablename__ = "lessons"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(50), nullable=False)
    grade: Mapped[int] = mapped_column(Integer, nullable=False)
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"), nullable=False)
    teacher_id: Mapped[int] = mapped_column(ForeignKey("teachers.id"), nullable=False)

    student: Mapped["Student"] = relationship("Student", back_populates="lessons")
    teacher: Mapped["Teacher"] = relationship("Teacher", back_populates="lessons")

    homework: Mapped["Homework"] = relationship(
        "Homework", back_populates="lesson", uselist=False
    )


    def __init__(
        self,
        name: str,
        description: str,
        student_id: int,
        teacher_id: int,
        grade: int = 0,
    ):
        self.name = name
        self.description = description
        self.student_id = student_id
        self.teacher_id = teacher_id
        self.grade = grade

    def __repr__(self):
        return f"Lesson(id={self.id}, name={self.name}, description={self.description})"
