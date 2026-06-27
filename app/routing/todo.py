from fastapi import APIRouter
from app.models.todo import CreateTodo


router = APIRouter(prefix="/todo")

@router.get("/")
def index():
    return {"message": "This is the todo router"}


@router.post("/")
def store(item:CreateTodo):
    return {"message": "Create a new ToDo item", "item":item.model_dump()}
