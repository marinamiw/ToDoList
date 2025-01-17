from pydantic import BaseModel

class Task(BaseModel):
    task:str

class TasksList(BaseModel):
    tasks: list[Task]