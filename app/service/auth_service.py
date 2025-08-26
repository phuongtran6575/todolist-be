from sqlmodel import Session, select
from models.user_model import User
import jwt
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_hash_password(password):
    return pwd_context.hash(password)

async def get_user_by_username(username: str, session: Session):
    statement = select(User).where(User.username == username)
    user_db = session.exec(statement).first()
    return user_db

async def registered(user:User ,session:Session):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user