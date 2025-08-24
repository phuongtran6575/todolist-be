from datetime import datetime
from pydantic import BaseModel

class TodoCreate(BaseModel):
    name: str
    due_at: datetime  # khai báo là datetime

data = {
    "name": "Đi tắm",
    "due_at": "2025-08-24T07:27:05.981Z"  # JSON string
}

todo = TodoCreate(**data)
print(todo.due_at, type(todo.due_at))
