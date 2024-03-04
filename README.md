# fastapi-project

## How to use
1. 가상환경 설정
```shell
cd fastapi-project
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
2. 서버 실행
```shell
uvicorn src.main:app --reload
```
3. 데이터 베이스를 위한 도커 컨테이너 실행
```shell
docker run -p 3306:3306 \
            -e MYSQL_ROOT_PASSWORD=todos \
            -e MYSQL_DATABASE=todos -d \
             -v todos:/db --name todos mysql:8.0
```