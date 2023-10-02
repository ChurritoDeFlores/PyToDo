## Import
from fastapi import FastAPI
from routes.user_route import Users
## punto de arranque (uvicorn index:index) --reload [para tener que ejecutar el comando cada vez que se realize un cambio]
index = FastAPI()

@index.get('/')
def getRoot():
    return "Hola esta es mi primer API"

## Incluir las rutas que vienen de el archivo user.py
index.include_router(Users)