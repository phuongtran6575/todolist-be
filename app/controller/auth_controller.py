from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from service import auth_service
from database.sqlite_database import SessionDepends
from models.user_model import User 


oauth2_schema = OAuth2PasswordBearer(tokenUrl="auth/token")
router = APIRouter(prefix="/auth", tags=["Auth"])

@router.get("/")
async def read_me(current_user= Annotated[str, Depends(oauth2_schema)]):
    return current_user

@router.post("/token")
async def login(session: SessionDepends,form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_db = await auth_service.get_user_by_username(form_data.username, session)
    if user_db.password == form_data.password:
        return {"access": user_db.username}

@router.post("/")
async def register(user:User, session: SessionDepends):
    return await auth_service.registered(user, session)