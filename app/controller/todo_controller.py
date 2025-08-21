from fastapi import APIRouter
from service.todo_service import get_all_todos, add_todo, update_todo, delete_todo
from service import todo_service
from database.sqlite_database import SessionDepends
from models.todo_model import Todo

router = APIRouter(prefix="/todos", tags=["Todo"])

@router.get("/")
async def get_all_todos(session: SessionDepends):
    return await todo_service.get_all_todos(session)

@router.get("/{todo_id}")
async def get_todo_by_id(todo_id:int,session: SessionDepends):
    return await todo_service.get_todo_by_id(todo_id, session)

@router.post("/")
async def add_todo(todo: Todo, session: SessionDepends):
    return await todo_service.add_todo(todo, session)

@router.put("/")
async def update_todo(todo: Todo, session: SessionDepends):
    return await todo_service.update_todo(todo, session)

@router.delete("/{todo_id}")
async def delete_todo(todo_id:int, session: SessionDepends):
    return await todo_service.delete_todo (todo_id, session)