from fastapi import APIRouter, Depends, HTTPException
from schema.request import LoginRequest, SignUpRequest
from schema.response import UserSchema
from database.orm import User
from database.repository import UserRepository
from service.user import UserService


router = APIRouter(prefix="/users")

@router.post("/sign-up", status_code=201)
def user_sign_up_handler(
    request: SignUpRequest,
    user_service: UserService = Depends(),
    user_repo: UserRepository = Depends()
):
    # 1. request body(username, password)
    # 2. password -> hashing -> hashed_password
    hashed_password = user_service.hash_password(
        plain_password=request.password
    )
    # 3. User(username, hashed_password)
    user: User = User.create(
        username=request.username, hashed_password=hashed_password
    )
    # 4. user -> db save
    user: User = user_repo.save_user(user=user) # id : int
    # 5. return user(id, username)
    return UserSchema.from_orm(user)

@router.post("/log-in")
def user_log_in_handler(
    request: LoginRequest,
    user_service: UserService = Depends(),
    user_repo: UserRepository = Depends()
):
    # 1. request body(username, password)
    # 2. db read user
    user: User | None =  user_repo.get_user_by_username(
        username=request.username
    )
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # 3. user.password, request.password -> bcrypt.checkpw
    verified: bool = user_service.verify_password(
        plain_password=request.password, hashed_password=user.hashed_password
    )

    if not verified:
        raise HTTPException(status_code=401, detail="Not Authorized")
    
    # 4. create jwt
    jwt = user_service.create_jwt(username=user.username)

    # 5. return jwt
    return jwt