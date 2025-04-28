from .students.students import router as students_router
from .users.users import router as users_router
from .authorization import router as auth_router
from .authorization.login import router as login_router
from .authorization.registration import router as reg_router