from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from service import auth_service
from service.todo_service import get_all_todos, add_todo, update_todo, delete_todo
from service import todo_service
from database.sqlite_database import SessionDepends
from models.todo_model import Todo

router = APIRouter(prefix="/todos", tags=["Todo"])
oauth2_schema = OAuth2PasswordBearer(tokenUrl="auth/token")
@router.get("/")
async def get_all_todos(token:Annotated[str, Depends(oauth2_schema)] ,session: SessionDepends ):
    current_user = auth_service.get_current_user(token, session)
    return await todo_service.get_all_todos(current_user.id, session, 1, 5)

@router.get("/{todo_id}")
async def get_todo_by_id(token: Annotated[str, Depends(oauth2_schema)] ,todo_id:int, session: SessionDepends):
    current_user = auth_service.get_current_user(token, session)
    todo = await todo_service.get_todo_by_id(current_user.id ,todo_id, session)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.post("/")
async def add_todo(token: Annotated[str, Depends(oauth2_schema)] ,todo: Todo, session: SessionDepends):
    current_user = auth_service.get_current_user(token, session)
    return await todo_service.add_todo(current_user.id ,todo, session)

@router.put("/{todo_id}")
async def update_todo( token: Annotated[str, Depends(oauth2_schema)] ,todo_id:int, todo: Todo, session: SessionDepends):
    current_user = auth_service.get_current_user(token, session)
    todo = await todo_service.update_todo(current_user.id, todo_id, todo, session)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.delete("/{todo_id}")
async def delete_todo( token: Annotated[str, Depends(oauth2_schema)] ,todo_id:int, session: SessionDepends):
    current_user = auth_service.get_current_user(token, session)
    todo = await todo_service.delete_todo (current_user.id, todo_id, session)
    if not todo:
        raise HTTPException(status_code=404, detail=" Todo not found")
    return todo