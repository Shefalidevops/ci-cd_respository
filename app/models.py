from typing import List, Optional
from .schemas import Todo, TodoCreate

class InMemoryTodoStore:
    def __init__(self) -> None:
        self._todos: List[Todo] = []
        self._next_id: int = 1

    def list_todos(self) -> List[Todo]:
        return self._todos

    def get_todo(self, todo_id: int) -> Optional[Todo]:
        return next((t for t in self._todos if t.id == todo_id), None)
    

    # def create_todo(self, payload: TodoCreate) -> Todo:
    #     todo = Todo(id=self._next_id, **payload.model_dump())
    #     self._next_id += 1
    #     self._todos.append(todo)
    #     return todo


    def create_todo(self, payload: TodoCreate) -> Todo:
        todo = Todo(id=self._next_id, **payload.model_dump())
        self._next_id += 1
        self._todos.append(todo)
        return todo


    def update_todo(self, todo_id: int, payload: TodoCreate) -> Optional[Todo]:
        todo = self.get_todo(todo_id)
        if todo is None:
            return None
        todo.title = payload.title
        todo.description = payload.description
        todo.completed = payload.completed
        return todo

    def delete_todo(self, todo_id: int) -> bool:
        todo = self.get_todo(todo_id)
        if todo is None:
            return False
        self._todos.remove(todo)
        return True

store = InMemoryTodoStore()
