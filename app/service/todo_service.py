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
    if not todo:
        return None
    return todo

async def add_todo(todo: Todo, session: Session):
    parse_due_at = datetime.fromisoformat(todo.due_at.replace("Z", "+00:00")) 
    todo_data= Todo(
        id = todo.id,
        description=todo.description,
        isDone= todo.isDone,
        name=todo.name,
        created_at=todo.created_at,
        due_at=parse_due_at
    )
    session.add(todo_data)
    session.commit()
    session.refresh(todo_data)
    return todo_data

async def update_todo(todo_id: int, todo: Todo, session: Session):
    statement = select(Todo).where(Todo.id == todo_id)
    todo_to_update = session.exec(statement).first()
    if not todo_to_update:
        return None   # hoặc raise HTTPException(404, "Todo not found")

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

async def delete_todo(todo_id: int, session: Session):
    statement = select(Todo).where(Todo.id == todo_id)
    todo = session.exec(statement).first()
    if not todo:
        return None
    session.delete(todo)
    session.commit()
    return {"status":"delete successfull",}