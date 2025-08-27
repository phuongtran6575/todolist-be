from datetime import datetime, timedelta, timezone
from sqlmodel import Session, select
from core.constants import ALGORITHM, SECRET_KEY
from models.user_model import User
import jwt
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(token: str, session: Session):
    
    return

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_hash_password(password):
    return pwd_context.hash(password)

async def get_user_by_username(username: str, session: Session):
    statement = select(User).where(User.username == username)
    user_db = session.exec(statement).first()
    return user_db

async def registered(user:User ,session:Session):
    hashed_pw = get_hash_password(user.password)
    user_db = User(username= user.username, password=hashed_pw)
    session.add(user_db)
    session.commit()
    session.refresh(user_db)
    return user_db

async def delete(user_id:int, session: Session):
    statement = select(User).where(user_id == User.id)
    user_db = session.exec(statement).first()
    session.delete(user_db)
    session.commit()
    return {"type": "delete"}
    