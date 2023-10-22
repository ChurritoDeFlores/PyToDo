from sqlalchemy import select
from fastapi import APIRouter, Response
from models.task_model import Task
from schemas.task_schema import tasks
from schemas.user_schema import users
from config.db import engine

Tasks = APIRouter()

## Crear
@Tasks.post('/tasks',tags = ['tasks'])
def Create_Task(t:Task):
    with engine.connect() as cnn:
        task = {}
        task['text'] = t.text
        task['user_id'] = t.user_id
        task['created_at'] = t.created_at
        task['completed_at'] = t.completed_at
        cnn.execute(tasks.insert().values(task))
        return ('okey')

# Listar Todo
@Tasks.get('/tasks',tags=['tasks'])
def List_Tasks():
    with engine.connect() as cnn:
        query = (
            select([tasks.c.id, tasks.c.text, users.c.name.label('user'), tasks.c.created_at, tasks.c.completed_at])
            .select_from(tasks.join(users, tasks.c.user_id == users.c.id))
        )
        return cnn.execute(query).fetchall()
# Listar uno
@Tasks.get('/task/{id}', response_model=Task,tags=['tasks'])
def List_Task(id : int):
    with engine.connect() as cnn:
        return cnn.execute(tasks.select().where(tasks.c.id == id)).first()

# Listar Tareas de un usuario
@Tasks.get('/tasks/{user_id}', response_model=list[Task],tags=['tasks'])
def List_Task(id : int):
    with engine.connect() as cnn:
        return cnn.execute(tasks.select().where(tasks.c.user_id == id)).fetchall()