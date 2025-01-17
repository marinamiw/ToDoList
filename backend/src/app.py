from http import HTTPStatus
from fastapi import FastAPI
from .schemas import Task, TasksList


app = FastAPI()

database = []

@app.post('/tasks', response_model=Task)
def create_task(newTask: Task):
    database.append(newTask)
    return newTask

@app.get('/tasks', response_model=TasksList)
def read_tasks():
    return {'tasks': database}