from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.models import create_data

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app = FastAPI()


# Определите функцию для включения маршрутизатора
def include_routers():
    from src.routers import students_router, users_router
    app.include_router(students_router, prefix="/students", tags=["students"])
    app.include_router(users_router, prefix="/users", tags=["users"])
    pass

# if __name__ == "__main__":
#     import uvicorn
#
#     include_routers()
#
#     app.add_middleware(
#         CORSMiddleware,
#         allow_origins=origins,
#         allow_credentials=True,
#         allow_methods=["*"],
#         allow_headers=["*"],
#     )
#     uvicorn.run(app, host="127.0.0.1", port=8000, workers=1)

include_routers()

create_data()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# uvicorn.run(app, host="127.0.0.1", port=8000, workers=1)
