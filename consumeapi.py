from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Create a model
class User(BaseModel):
    name: str
    age: int

@app.get("/")
def home():
    return {"message": "Welcome"}

#Create the POST endpoint
@app.post("/users")
def create_user(user: User):
    return {
        "message": "Created",
        "user": user
    }

#Update existing data.
@app.put("/users/{id}")
def update_user(id: int, user: User):
    return {
        "id": id,
        "user": user
    }
#Delete data
@app.delete("/users/{id}")
def delete_user(id: int):
    return {
        "message": f"Deleted user {id}"
    }