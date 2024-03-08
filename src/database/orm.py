from re import T
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import declarative_base

from schema.request import CreateToDoRequest

Base = declarative_base()

class ToDo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, index=True)
    contents = Column(String(256), nullable=False)
    is_done = Column(Boolean, nullable=False)

    # 객체를 출력할 때 보기 쉬운 형태로 보기 위해서 repr이라는 magic method를 override
    def __repr__(self):
        return f"Todo(id={self.id}, contents={self.contents}, is_done={self.is_done})"
    
    # Class variable에 access하기 위한 class method
    @classmethod
    def create(cls, request: CreateToDoRequest) -> "ToDo":
        return cls(
            contents=request.contents,
            is_done=request.is_done
        )
    
    # 유지보수의 편의성을 위해 instance method 정의
    # 전체적인 시스템의 안정성을 위해 일반적으로 데이터를 변경할 때는 instance method를 이용하는 것이 좋다.
    def done(self) -> "ToDo":
        self.is_done = True
        return self

    def undone(self) -> "ToDo":
        self.is_done = False
        return self