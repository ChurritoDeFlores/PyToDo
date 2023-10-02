from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED
from models.user_model import User
from schemas.user_schema import users
from config.db import engine
from sqlalchemy import select
from cryptography.fernet import Fernet

Users = APIRouter()
## Funcion de encriptacion
key = Fernet.generate_key()
f = Fernet(key)

## Listar todo
@Users.get('/users')
def List_Users():
    pass

## Listar uno
@Users.get('/users/{id}')
def List_User(id:int):
    return f"Usuario con ID= {id}"
## Crear
@Users.post('/users')
def Create_User(user: User, status_code=HTTP_201_CREATED):
    with engine.connect() as cnn:
        ## Creo un diccionario del nuevo usuario
        new_user={}
        new_user['name']= user.name
        ## Se encripta la contraseña del usuario
        new_user['password'] = f.encrypt(user.password.encode("utf-8"))
        new_user['role'] = user.role
        new_user['status'] = user.status
        new_user['created_at'] = user.created_at
        cnn.execute(users.insert().values(new_user))
        cnn.commit()
        return Response(status_code)

## Eliminar
@Users.delete('/users/{id}')
def Delete_User(id: int):
    return f"Eliminar el usuario de ID= {id}"

## Modificar
@Users.put('/uAsers/{id}')
def Update_User(id:int, new_user: User):
    return f"El usuario de Id= {id}, se ha modificado con los datos: {new_user}"