from datetime import datetime
from models.todo_model import Todo
from sqlmodel import Session, select

async def get_all_todos(user_id:int, session: Session, ):
    statement = select(Todo).where(Todo.user_id == user_id)
    todos = session.exec(statement).all()
    return todos

async def get_todo_by_id( user_id: int, todo_id: int, session: Session,):
    statement = select(Todo).where(Todo.id == todo_id)
    todo = session.exec(statement).first()
    if not todo or todo.user_id != user_id:
        return None
    return todo

async def add_todo(user_id:int, todo: Todo, session: Session, ):
    parse_due_at = datetime.fromisoformat(todo.due_at.replace("Z", "+00:00")) 
    parse_created_at = datetime.fromisoformat(todo.created_at.replace("Z", "+00:00"))
    todo_data= Todo(
        id = todo.id,
        description=todo.description,
        isDone= todo.isDone,
        name=todo.name,
        #created_at=todo.created_at,
        created_at=parse_created_at,
        due_at=parse_due_at,
        user_id=user_id
    )
    session.add(todo_data)
    session.commit()
    session.refresh(todo_data)
    return todo_data

async def update_todo( user_id: int, todo_id: int, todo: Todo, session: Session,):
    statement = select(Todo).where(Todo.id == todo_id)
    todo_to_update = session.exec(statement).first()
    if not todo_to_update or todo_to_update.user_id != user_id:
        return None   

    # parse datetime
    parse_due_at = datetime.fromisoformat(todo.due_at.replace("Z", "+00:00"))

    # update fields
    todo_to_update.description = todo.description
    todo_to_update.isDone = todo.isDone
    todo_to_update.due_at = parse_due_at
    todo_to_update.name = todo.name

    session.add(todo_to_update)
    session.commit()
    session.refresh(todo_to_update)
    return todo_to_update

async def delete_todo(user_id:int, todo_id: int, session: Session, ):
    statement = select(Todo).where(Todo.id == todo_id)
    todo = session.exec(statement).first()
    if not todo or todo.user_id != user_id:
        return None
    session.delete(todo)
    session.commit()
    return {"status":"delete successfull",}