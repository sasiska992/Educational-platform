from typing import Type, Any, Optional

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import DeclarativeBase

from src.models import Session


class Base(DeclarativeBase):
    def add(self):
        try:
            with Session() as session:
                session.add(self)
                session.commit()
        except SQLAlchemyError as e:
            print(f"Error adding object: {e}")

    @staticmethod
    def delete(obj):
        try:
            with Session() as session:
                session.delete(obj)
                session.commit()
        except SQLAlchemyError as e:
            print(f"Error deleting object: {e}")

    def update_values(self, **kwargs):
        try:
            with Session() as session:
                existing_object = session.query(type(self)).get(self.id)
                if existing_object is None:
                    print("Объект не найден.")
                    return

                for key, value in kwargs.items():
                    setattr(existing_object, key, value)  # Обновляем атрибуты объекта

                session.commit()  # Коммитим изменения один раз
        except SQLAlchemyError as e:
            print(f"Error updating values: {e}")
            session.rollback()  # Откатываем изменения в случае ошибки

    @classmethod
    def select_for_one_key(cls, column: str, value: Any):
        """Выбирает один объект по заданному ключу."""
        try:
            with Session() as session:
                result = session.query(cls).filter(getattr(cls, column) == value).first()
                return result
        except SQLAlchemyError as e:
            print(f"Error selecting object: {e}")
            return None

    @classmethod
    def select_for_all(self):
        """Выбирает все объекты типа cls."""
        try:
            with Session() as session:
                result = session.query(self).all()
                return result
        except SQLAlchemyError as e:
            print(f"Error selecting object: {e}")