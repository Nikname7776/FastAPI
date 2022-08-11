from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base

"""Таблица для данных"""


class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    # Внешний ключ, метка для отношения
    user_id = Column(Integer, ForeignKey('users.id'))

    # устанавливаем отношение конкретных полей таблицы к пользователю
    creator = relationship("User", back_populates="blogs")


"""Таблица данных пользователя"""


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship("Blog", back_populates="creator")
