from datetime import datetime
from models.todo_model import Todo
from sqlmodel import Session, select

async def get_all_todos(session: Session):
    statement = select(Todo)
    todos = session.exec(statement).all()
    return todos

async def get_todo_by_id(todo_id: int, session: Session):
    statement = select(Todo).where(Todo.id == todo_id)
    todo = session.exec(statement).first()
    return todo

async def add_todo(todo: Todo, session: Session):
    parse_created_at = datetime.fromisoformat(todo.created_at.replace("Z", "+00:00")) 
    parse_due_at = datetime.fromisoformat(todo.due_at.replace("Z", "+00:00")) 
    todo_data= Todo(
        id = todo.id,
        description=todo.description,
        isDone= todo.isDone,
        name=todo.name,
        created_at=parse_created_at,
        due_at=parse_due_at
    )
    session.add(todo_data)
    session.commit()
    session.refresh(todo_data)
    return todo_data

async def update_todo(todo: Todo, session: Session):
    statement = select.select(Todo).where(Todo.id == todo.id)
    todo_to_update = session.exec(statement).first()
    todo_to_update.name = todo.name
    session.add(todo_to_update)
    return todo_to_update

async def delete_todo(todo_id: int, session: Session):
    statement = select(Todo).where(Todo.id == todo_id)
    todo = session.exec(statement).first()
    session.delete(todo)
    session.commit()
    return {"delete"}