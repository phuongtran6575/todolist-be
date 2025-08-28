from datetime import datetime
from sqlmodel import Relationship, SQLModel, Field
from typing import Optional

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: Optional[str]
    password: Optional[str]

    todos: list["Todo"] = Relationship(back_populates="owner")  # dùng "todos" (số nhiều)

class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    description: Optional[str]
    name: Optional[str]
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    due_at: Optional[datetime]
    isDone: Optional[bool]

    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    owner: Optional[User] = Relationship(back_populates="todos")  # khớp với "todos"
