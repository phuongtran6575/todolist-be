import datetime
from sqlmodel import SQLModel, Field
class Todo(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    description: str
    name: str
    created_ad:  datetime = Field(default_factory=datetime.utcnow)
    due_at: datetime 
    isDone: bool