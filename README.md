# fastapi-project

## How to use
1. 가상환경 설정 (도커 파일도 추가 예정)
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