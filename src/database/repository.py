from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import select
from database.orm import ToDo

def get_todos(session: Session) -> List[ToDo]:
    return list(session.scalars(select(ToDo)))