from fastapi import APIRouter, Depends, HTTPException
from api.auth import schema, crud
from api.utils import cryptoUtil, jwtUtil, constantUtil
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()


@router.post("/auth/register", response_model=schema.UserList)
async def register(user: schema.UserCreate):
    # Check user exists
    result = await crud.find_exist_user(user.email)
    if result:
        raise HTTPException(status_code=409, detail="User already registered.")
    # Create new user
    # hash password
    user.password = cryptoUtil.hash_password(user.password)
    await crud.save_user(user)
    return {**user.dict()}


@router.post("/auth/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Check user existed
    result = await crud.find_exist_user(form_data.username)
    if not result:
        raise HTTPException(status_code=404, detail="User not found.")

    # Verify password
    user = schema.UserCreate(**result)
    verified_password = cryptoUtil.verify_password(form_data.password, cryptoUtil.hash_password(user.password))
    if not verified_password:
        raise HTTPException(status_code=404, detail="Incorrect username or password.")

    # Create Token
    access_token_expires = jwtUtil.timedelta(minutes=constantUtil.ACCESS_TOKEN_EXPIRE_MINUTE)
    access_token = await jwtUtil.create_access_token(
        data={"sub": form_data.username},
        expires_delta=access_token_expires
    )
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
