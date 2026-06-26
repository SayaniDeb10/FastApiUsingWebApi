from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()

#Temporary Storage
users = []
next_user_id = 1

class User(BaseModel):
    name:str
    age:int

@app.post("/users")
def create_user(user:User):
    global next_user_id

    new_user ={
        "user_id": next_user_id,
        "name": user.name,
        "age" : user.age
    }

    users.append(new_user)
    next_user_id +=1

    return {
        "message": "User Created Successfully",
        "user": new_user
    }

@app.get("/users")
def view_user():
    return users


@app.put("/users/{user_id}")
def user_update(user_id:int , user:User):
    for item in users:
        if item["user_id"] == user_id:
            item["name"] = user.name
            item["age"] = user.age
            return {
                "message" : "UserUpdated Successfully",
                "user": item
            }
        raise HTTPException(status_code=404, detail="User Not Found")
    

@app.delete("/users/{user_id}")
def delete_user(user_id: int):

    for item in users:
        if item["user_id"] == user_id:
            users.remove(item)
            return {
                "message": "User deleted"
            }

    raise HTTPException(status_code=404, detail="User not found")