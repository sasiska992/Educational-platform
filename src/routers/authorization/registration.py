from fastapi import APIRouter, HTTPException, Request, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from src.models.users import User
from . import router
from src.routers import templates


@router.get("/registration", response_class=HTMLResponse)
async def registration(request: Request):
    return templates.TemplateResponse("registration.html", {"request": request})


@router.post("/registration")
async def register(
    request: Request,
    first_name: str = Form(...),
    last_name: str = Form(...),
    password: str = Form(...),
    confirm_password: str = Form(...),
):

    if password != confirm_password:
        raise HTTPException(status_code=400, detail="Пароли не совпадают")

    try:
        user = User(name=first_name, lastname=last_name, password=password)
        user.add()
        return RedirectResponse(url="/auth/", status_code=status.HTTP_303_SEE_OTHER)

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
