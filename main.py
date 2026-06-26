from fastapi import FastAPI, Depends
from typing import Annotated
from test import QueryParams

app = FastAPI()

@app.get("/")
def root(query: Annotated[QueryParams, Depends()]):
    return {"message": "Hello FastAPI", "params": query}

@app.get("/predict")
def predict_model(age : int, sex: str):
    if age<15 or sex == "F":
        return {'survived':1}
    else:
        return {'survived':0}