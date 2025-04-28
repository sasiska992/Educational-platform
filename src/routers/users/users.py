from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from src.models.users import User

# Укажите путь к папке с шаблонами
templates = Jinja2Templates(directory="src/templates")


router = APIRouter(tags=["users"])

@router.get("/get_all_users")
def get_users():
    users:list[User] = User.select_for_all()
    return {"users": users}

@router.post("/create_user/{name}/{lastname}/{password}")
def create_user(name: str,lastname: str, password: str):
    user = User(name=name, lastname=lastname, password=password)
    user.add()
    return {"message": "User created"}

