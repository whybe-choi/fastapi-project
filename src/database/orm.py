from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String(256), nullable=False)
    is_done = Column(Boolean, nullable=False)

    # 객체를 출력할 때 보기 쉬운 형태로 보기 위해서 repr이라는 magic method를 override
    def __repr__(self):
        return f"Todo(id={self.id}, content={self.content}, is_done={self.is_done})"