from fastapi import APIRouter, HTTPException
from auth.dto.request.login import LoginDto
from auth.dto.request.register import RegisterDto
from auth.functions.create_token import create_access_token
from auth.functions.hash_user_password import hash_password
from shared.dto.response.api_responseDto import SuccessResponseDto
from users.repository import UserRepository
from auth.functions.verify_user_password import verify_password

router = APIRouter()
userRepo = UserRepository()


@router.post("/login", response_model=SuccessResponseDto)
def login(data: LoginDto):
    user = userRepo.findByUsername(data.username)

    if user is None:
        raise HTTPException(400, detail="نام کاربری یا رمز عبور اشتباه است")

    if verify_password(data.password, user["password"]) is False:
        raise HTTPException(400, detail="نام کاربری یا رمز عبور اشتباه است")

    token = create_access_token({"id": user["id"], "username": user["username"]})

    del user["password"]

    return {
        "data": {"token": token, "user": user},
        "message": "ورود با موفقیت انجام شد",
    }


@router.post("/register", response_model=SuccessResponseDto)
def register(data: RegisterDto):
    user = userRepo.findByUsername(data.username)

    if user:
        raise HTTPException(400, detail="نام کاربری تکراری است")

    if len(data.password) < 4:
        raise HTTPException(400, detail="رمز عبور باید حداقل 4 کاراکتر باشد")

    data.password = hash_password(data.password)

    user = userRepo.createOne(data)

    del user["password"]

    return {
        "data": user,
        "message": "ثبت نام با موفقیت انجام شد",
    }
