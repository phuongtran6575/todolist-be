import os
from sqlmodel import create_engine, SQLModel, Session
from typing import Annotated
from fastapi import Depends   # bạn cần import Depends nếu dùng trong FastAPI

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./todo.db")
engine = create_engine("sqlite:///todo.db", echo=True)


def get_session():
    with Session(engine) as session:
        yield session

SessionDepends = Annotated[Session, Depends(get_session)]
