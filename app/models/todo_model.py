from datetime import datetime
from sqlmodel import SQLModel, Field
from typing import Optional

class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    description: Optional[str]
    name: Optional[str]
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    due_at: Optional[datetime]
    isDone: Optional[bool]