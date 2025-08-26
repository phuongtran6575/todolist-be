from sqlmodel import SQLModel

class User(SQLModel):
    id: int
    username: str
    password: str