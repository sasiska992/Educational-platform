from fastapi import APIRouter

from src.models.students import Student
from src.models import Session

router = APIRouter(tags=["students"])

@router.get("/get_all_students")
def get_students():    
    # students:list[Student] = Student.select_for_all()
    with Session() as session:
        students = session.query(Student).all()
        students[0].user
    return {"students": students}

@router.post("/create_student/{user_id}")
def create_student(user_id: int):
    student = Student(user_id=user_id)
    student.add()
    return {"message": "Student created"}