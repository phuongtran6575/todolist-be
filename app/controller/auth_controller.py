from datetime import timedelta
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from core.constants import ACCESS_TOKEN_EXPIRE_MINUTES
from service import auth_service
from database.sqlite_database import SessionDepends
from models.todo_model import User 


oauth2_schema = OAuth2PasswordBearer(tokenUrl="auth/token")
router = APIRouter(prefix="/auth", tags=["Auth"])

@router.get("/me")
async def read_me(token: Annotated[str, Depends(oauth2_schema)] ,session: SessionDepends):
    current_user = auth_service.get_current_user(token, session)
    return {"id": current_user.id, "username": current_user.username}

@router.post("/token")
async def login(session: SessionDepends,form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_db = await auth_service.get_user_by_username(form_data.username, session)
    
    if not user_db or not auth_service.verify_password(form_data.password, user_db.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Sai tên đăng nhập hoặc mật khẩu") 
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth_service.create_access_token(data = {"sub":str(user_db.id)}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/")
async def register(user:User, session: SessionDepends):
    return await auth_service.registered(user, session)

@router.delete("/{user_id}")
async def delete_user(user_id: int, session:SessionDepends):
    return await auth_service.delete(user_id, session)