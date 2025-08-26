from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm 


oauth2_schema = OAuth2PasswordBearer(tokenUrl="auth/token")
router = APIRouter(prefix="/auth", tags=["Auth"])

@router.get("/")
async def get_user_by_username():
    return

@router.post("/token")
async def login():
    return

@router.post("/")
async def register():
    return