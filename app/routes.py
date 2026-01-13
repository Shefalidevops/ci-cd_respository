from fastapi import APIRouter, HTTPException, status
from typing import List
from .schemas import Todo, TodoCreate
from .models import store

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "ok"}

@router.get("/todos", response_model=List[Todo])
def list_todos():
    return store.list_todos()

@router.post("/todos", response_model=Todo, status_code=status.HTTP_201_CREATED)
def create_todo(payload: TodoCreate):
    return store.create_todo(payload)

@router.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    todo = store.get_todo(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, payload: TodoCreate):
    todo = store.update_todo(todo_id, payload)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int):
    deleted = store.delete_todo(todo_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Todo not found")
    return None
