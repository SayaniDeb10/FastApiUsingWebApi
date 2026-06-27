from fastapi import FastAPI, Depends
from typing import Annotated
from test import QueryParams
from app.routing import todo
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

# Includes all routes

app = FastAPI()

app.include_router(todo.router)

@app.exception_handler(RequestValidationError)
async def validation_exception_header(request,exc):
    errors = {}
    for error in exc.errors():
        print(f"The error is: {error}")
        errors[error['loc'][-1]] = error['msg']
    return JSONResponse(
        status_code=422,
        content={
            "message": "Validation Error",
            "errors": errors
        }
)

@app.get("/")
def root(query: Annotated[QueryParams, Depends()]):
    return {"message": "Hello FastAPI", "params": query}

# @app.get("/predict")
# def predict_model(age : int, sex: str):
#     if age<15 or sex == "F":
#         return {'survived':1}
#     else:
#         return {'survived':0}