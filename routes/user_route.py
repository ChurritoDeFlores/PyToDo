from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED,HTTP_204_NO_CONTENT,HTTP_202_ACCEPTED
from models.user_model import User
from schemas.user_schema import users
from config.db import engine
from cryptography.fernet import Fernet

Users = APIRouter()
## Funcion de encriptacion
key = Fernet.generate_key()
f = Fernet(key)

## Listar todo
@Users.get('/users')
def List_Users():
    with engine.connect() as cnn:
        return cnn.execute(users.select()).fetchall()

## Listar uno
@Users.get('/users/{id}')
def List_User(id:int):
    with engine.connect() as cnn:
        return cnn.execute(users.select().where(users.c.id == id)).first()

## Verificar FALTA REALIZAR METODO PARA VERIFICAR
@Users.get('/users/')
def UserOK(name:str, password:str):
    with engine.connect() as cnn:
        user = cnn.execute(users.select().where(users.c.name == name)).first()
        if (True):
            return {'user_exist':'true'}
    return {'user_exist':'false'}

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
        return Response(status_code)

## Eliminar
@Users.delete('/users/{id}')
def Delete_User(id: int, status_code=HTTP_204_NO_CONTENT):
    with engine.connect() as cnn:
        if cnn.execute(users.select().where(users.c.id == id)).first():
            cnn.execute(users.delete().where(users.c.id == id))
            return Response(status_code)

## Modificar
@Users.put('/users/{id}')
def Update_User(id:int, new_user: User, status_code=HTTP_202_ACCEPTED):
    with engine.connect() as cnn:
        ## Creo un diccionario del nuevo usuario
        user={}
        user['name']= new_user.name
        ## Se encripta la contraseña del usuario
        user['password'] = f.encrypt(new_user.password.encode("utf-8"))
        user['role'] = new_user.role
        user['status'] = new_user.status
        user['created_at'] = new_user.created_at
        cnn.execute(users.update().where(users.c.id == id).values(user))
        return Response(status_code)