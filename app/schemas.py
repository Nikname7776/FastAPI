from typing import List
from typing import Union

from pydantic import BaseModel

"""Схема для работы с БД (фильмов и описания)"""


# Схема для работы с полученными данными
class Blog(BaseModel):
    title: str
    body: str

    class Config:
        orm_mode = True


# Схема для передачи данных без id


"""Схема для работы с пользователем"""


class User(BaseModel):
    name: str
    email: str
    password: str


"""Схема для работы с пользователем"""


# Схема для передачи данных без пароля
class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []

    class Config:
        orm_mode = True  # чтобы работать с sql данными, т.к. по дефолту pydantic принимает словари


"""Схема для работы с БД (фильмов и описания)"""


class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser

    class Config:
        orm_mode = True  # чтобы работать с sql данными, т.к. по дефолту pydantic принимает словари


"""Схема для регистрации пользователя"""


class Login(BaseModel):
    username: str
    password: str


"""Схема для создания токена"""


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Union[str, None] = None
