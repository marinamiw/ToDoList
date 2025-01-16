from http import HTTPStatus
from fastapi import FastAPI
from .schemas import Task


app = FastAPI()

@app.post('/tasksend', response_model=Task)
def create_task(newTask: Task):
    return newTask