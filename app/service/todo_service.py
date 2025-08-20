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
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo

async def update_todo(todo: Todo, session: Session):
    statement = select.todo(Todo).where(Todo.id == todo.id)
    todo_to_update = session.exec(statement).first()
    todo_to_update.name = todo.name
    session.add(todo_to_update)
    return todo_to_update

async def delete_todo(todo_id: int, session: Session):
    statement = select.todo(Todo).where(Todo.id == todo_id)
    todo = session.exec(statement).first()
    session.delete(todo)
    session.commit()
    return {"delete"}