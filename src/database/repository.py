from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy import select, delete
from database.connection import get_db
from database.orm import ToDo, User

class ToDoRepository:
    def __init__(self, session: Session = Depends(get_db)):
        self.session = session

    def get_todos(self) -> List[ToDo]:
        return list(self.session.scalars(select(ToDo)))

    def get_todo_by_todo_id(self, todo_id: int) -> ToDo | None:
        return self.session.scalar(select(ToDo).where(ToDo.id == todo_id))

    def create_todo(self, todo: ToDo) -> ToDo:
        self.session.add(instance=todo)
        self.session.commit()
        self.session.refresh(instance=todo)
        return todo

    def update_todo(self, todo: ToDo) -> ToDo:
        self.session.add(instance=todo)
        self.session.commit() # db save
        self.session.refresh(instance=todo) # # db read
        return todo

    def delete_todo(self, todo_id: int) -> None:
        self.session.execute(delete(ToDo).where(ToDo.id == todo_id))
        self.session.commit()
        return None
    
class UserRepository:
    def __init__(self, session: Session = Depends(get_db)):
        self.session = session

    def save_user(self, user: User) -> User:
        self.session.add(instance=user)
        self.session.commit()
        self.session.refresh(instance=user)
        return user