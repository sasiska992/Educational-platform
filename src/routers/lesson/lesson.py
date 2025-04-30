from fastapi import APIRouter, Request, status, Form

from fastapi import status
from pydantic import BaseModel
from fastapi.responses import HTMLResponse, RedirectResponse
from src.models.homework import Homework
from src.routers import templates
from src.models.lessons import Lesson
from src.models import Session

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def lesson(request: Request):
    lessons = Lesson.select_for_all()

    return templates.TemplateResponse(
        "lessons.html", {"request": request, "lessons": lessons}
    )


@router.get("/create_lesson", response_class=HTMLResponse)
def create_lesson(request: Request):
    return templates.TemplateResponse("create_lesson.html", {"request": request})


@router.post("/create_lesson", response_class=HTMLResponse)
def create_lesson(
    request: Request, name: str = Form(...), description: str = Form(...)
):
    lesson = Lesson(name=name, description=description, student_id=1, teacher_id=1)
    lesson.add()
    return RedirectResponse(url="/lesson/", status_code=status.HTTP_303_SEE_OTHER)


@router.get("/lesson/{lesson_id}", response_class=HTMLResponse)
async def lesson(request: Request, lesson_id: int):
    with Session() as session:
        lesson = session.query(Lesson).filter(Lesson.id == lesson_id).first()
        homeworks = (
            session.query(Homework).filter(Homework.lesson_id == lesson_id).all()
        )
        lesson.homeworks = homeworks
    return templates.TemplateResponse(
        "lesson.html", {"request": request, "lesson": lesson}
    )


class HomeworkCreate(BaseModel):
    title: str
    description: str
    lesson_id: str


@router.post(
    "/create_homework",
    status_code=status.HTTP_201_CREATED,
    responses={
        422: {"description": "Validation Error"},
        500: {"description": "Internal Server Error"},
    },
)
async def create_homework(form_homework: HomeworkCreate) -> dict:
    """
    Создание нового домашнего задания

    - **title**: Название (3-100 символов)
    - **description**: Описание (мин. 10 символов)
    - **lesson_id**: ID урока (положительное число)
    """
    homework = Homework(
        name=form_homework.title,
        description=form_homework.description,
        lesson_id=form_homework.lesson_id,
    )
    homework.add()
    return {
        "id": homework.id,
        "title": homework.name,
        "description": homework.description,
    }


class CheckHomework(BaseModel):
    grade: str
    lesson_id: str


@router.post("/check_homework")
async def check_homework(data: CheckHomework):
    lesson_id = int(data.lesson_id)
    grade = int(data.grade)
    with Session() as session:
        lesson: Lesson = session.query(Lesson).filter(Lesson.id == lesson_id).first()
        lesson.grade = grade
        session.commit()
    return {"status": "200", "message": "Оценка успешно отправлена"}
