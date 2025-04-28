from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from src.models.users import User
from . import router

# Укажите путь к папке с шаблонами
templates = Jinja2Templates(directory="src/templates")


print('hello from login')

@router.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})