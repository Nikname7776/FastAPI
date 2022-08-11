from fastapi import FastAPI

from app.routers import blog, authentication
from app.routers import users
from . import models
from .database import engine

app = FastAPI()

models.Base.metadata.create_all(engine)  # создаёт таблицу в соответствии с моделью

app.include_router(authentication.router)  # Маршрут
app.include_router(blog.router)  # Маршрут
app.include_router(users.router)  # Маршрут
