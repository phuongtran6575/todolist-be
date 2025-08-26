from sqlmodel import Session, select
from models.user_model import User

async def get_user_by_username(username: str, session: Session):
    statement = select(User).where(User.username == username)
    user_db = session.exec(statement).first()
    return user_db



async def registered(user:User ,session:Session):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user