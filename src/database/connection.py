from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from orm import ToDo

DATABASE_URL = "mysql+pymysql://root:todos@127.0.0.1:3306/todos"

engine = create_engine(DATABASE_URL, echo=True)
SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# api에서 이용할 generator
# FastAPI에서 request가 들어왔을 때 session이 생성되어 yield 함수를 호출하면 생성된 session이 반환된다.
# 응답을 한 이후에 session을 close하며 FastAPI가 session을 관리한다.
def get_db():
    session = SessionFactory()
    try:
        yield session
    finally:
        session.close()