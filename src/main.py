from fastapi import FastAPI

app = FastAPI()

# FastAPI 서버에 root path로 get 요청을 보내면 아래의 함수가 실행되어 api 응답을 보낸다.
@app.get("/")
def health_check_handler():
    return {"ping" : "pong"}


todo_data = {
    1: {
        "id" : 1,
        "content" : "실전! FastAPI 섹션 0 수강",
        "is_done" : True,
    },
    2: {
        "id" : 2,
        "content" : "실전! FastAPI 섹션 1 수강",
        "is_done" : False,
    },
    3: {
        "id" : 3,
        "content" : "실전! FastAPI 섹션 2 수강",
        "is_done" : False,
    },
}

@app.get("/todos")
def get_todos_handler():
    return list(todo_data.values())
