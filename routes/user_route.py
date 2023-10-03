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
@Users.get('/users', response_model=list[User],tags=['users'])
def List_Users():
    with engine.connect() as cnn:
        return cnn.execute(users.select()).fetchall()

## Listar uno
@Users.get('/users/{id}', response_model=User,tags=['users'])
def List_User(id:int):
    with engine.connect() as cnn:
        return cnn.execute(users.select().where(users.c.id == id)).first()

## Verificar FALTA REALIZAR METODO PARA VERIFICAR
@Users.get('/users/',tags=['users'])
def UserOK(name:str, password:str):
    if validate_user_password(name, password):
        return {'user_exist': True}
    else:
        return {'user_exist': False}

## Crear
@Users.post('/users',tags=['users'])
def Create_User(user: User, status_code=HTTP_201_CREATED):
    file_error={'name':True,'password':True}
    if user.name is None:
        file_error['name']=False
    if user.password is None:
        file_error['password']=False
    if file_error['name'] & file_error['password']:
        with engine.connect() as cnn:
            # Creo un diccionario de campos a actualizar
            fields_to_create = {}
            fields_to_create['name'] = user.name
            encrypted_password = f.encrypt(user.password.encode("utf-8"))
            fields_to_create['password'] = encrypted_password
            # Comprueba si se proporciona el rol (DEBERIA DE VERIFICAR QUE LOS ROLES EXISTAN ANTES DE CAMBIARLO)
            if user.role is not None:
                fields_to_create['role'] = user.role
            # Comprueba si se proporciona el estado
            if user.status is not None:
                fields_to_create['status'] = user.status
            cnn.execute(users.insert().values(**fields_to_create))
            return Response(status_code)
    else:
        text_name = ''
        text_password = ''
        if not file_error['name']:
            text_name = '- nombre -'
        if not file_error['password']:
            text_password = '- contraseña -'
        return {'Error': f'El campo {text_name} {text_password} no fue completado'}

## Eliminar
@Users.delete('/users/{id}',tags=['users'])
def Delete_User(id: int, status_code=HTTP_204_NO_CONTENT):
    with engine.connect() as cnn:
        if cnn.execute(users.select().where(users.c.id == id)).first():
            cnn.execute(users.delete().where(users.c.id == id))
            return Response(status_code)

## Modificar
@Users.put('/users/{id}',tags=['users'])
def Update_User(id:int, new_user: User, status_code=HTTP_202_ACCEPTED):
    with engine.connect() as cnn:
        # Creo un diccionario de campos a actualizar
        fields_to_update = {}
        # Compruebo si se proporciona el nombre
        if new_user.name is not None:
            fields_to_update['name'] = new_user.name
        # Comprueba si se proporciona la contraseña
        if new_user.password is not None:
            encrypted_password = f.encrypt(new_user.password.encode("utf-8"))
            fields_to_update['password'] = encrypted_password
        # Comprueba si se proporciona el rol (DEBERIA DE VERIFICAR QUE LOS ROLES EXISTAN ANTES DE CAMBIARLO)
        if new_user.role is not None:
            fields_to_update['role'] = new_user.role
        # Comprueba si se proporciona el estado
        if new_user.status is not None:
            fields_to_update['status'] = new_user.status
        # Compruebo si se proporciona la fecha de creación (NO SE PUEDE MODIFICAR LA FECHA DE CREACION DEL USUARIO)
        ##if new_user.created_at is not None:
        ##    fields_to_update['created_at'] = new_user.created_at
        # Realizo la actualización en la base de datos
        cnn.execute(users.update().where(users.c.id == id).values(**fields_to_update))
        return Response(status_code)
    
## Metodos Adicionales
def validate_user_password(name, password):
    with engine.connect() as cnn:
        # Busco el usuario por nombre
        user = cnn.execute(users.select().where(users.c.name == name)).first()
        # Si no se encuentra el usuario, devuelve False
        if user is None:
            return False
        # Desencripto la contraseña almacenada en la base de datos
        decrypted_password = f.decrypt(user['password'].encode("utf-8")).decode("utf-8")
        # Compara la contraseña proporcionada con la contraseña almacenada
        if password == decrypted_password:
            return True
    # Si no se cumple ninguna de las condiciones anteriores, devuelve False
    return False