from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

tasks = []

class Task(BaseModel):
    title: str
    done: bool = False

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return task

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    tasks[task_id] = updated_task
    return updated_task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    tasks.pop(task_id)
    return {"message": "Task deleted"}