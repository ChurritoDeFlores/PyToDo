# Imports
from fastapi import APIRouter, Response
from models.role_model import Role
from schemas.role_schema import roles
from config.db import engine

Roles = APIRouter()

## Metodos

# Crear
@Roles.post('/roles', tags=['roles'])
def Create_Role(r:Role):
    with engine.connect() as cnn:
        role = {}
        role['name'] = r.name
        role['status'] = r.status
        cnn.execute(roles.insert().values(role))
        return ('okey')

# Listar Todo
@Roles.get('/roles', response_model=list[Role],tags=['roles'])
def List_Roles():
    with engine.connect() as cnn:
        return cnn.execute(roles.select()).fetchall()
# Listar uno
@Roles.get('/roles/{id}', response_model=Role,tags=['roles'])
def List_Role(id : int):
    with engine.connect() as cnn:
        return cnn.execute(roles.select().where(roles.c.id == id)).first()