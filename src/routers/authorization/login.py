from fastapi import APIRouter, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from src.models import Session
from src.models.users import User
from . import router
from src.routers import templates


@router.get("/", response_class=HTMLResponse)
async def index_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.post("/login")
def login(
    request: Request,
    first_name: str = Form(...),
    last_name: str = Form(...),
    password: str = Form(...),
):
    with Session() as session:
        user = (
            session.query(User)
            .filter(User.name == first_name, User.lastname == last_name)
            .first()
        )
        if not user.check_password(password):
            return {"code": "401", "message": "Incorrect username or password"}
    return RedirectResponse(url="/lesson/", status_code=status.HTTP_303_SEE_OTHER)
