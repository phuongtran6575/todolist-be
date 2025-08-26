from sqlmodel import Session, select
from models.user_model import User

async def get_user_by_username(username: str, session: Session):
    statement = select(User).where(User.username == username)
    user_db = session.exec(statement).first()
    return user_db

async def login():
    return

async def register():
    return