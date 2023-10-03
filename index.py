## Import
from fastapi import FastAPI
from routes.user_route import Users
from routes.role_route import Roles
from routes.task_route import Tasks
from starlette.responses import HTMLResponse
import os
## punto de arranque (uvicorn index:index) --reload [para tener que ejecutar el comando cada vez que se realize un cambio]
index = FastAPI()

@index.get('/', response_class=HTMLResponse)
def getRoot():
    with open(os.path.join(os.path.dirname(__file__), 'template/index.html'), 'r') as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

## Incluir las rutas que vienen de el archivo user.py
index.include_router(Users)
index.include_router(Roles)
index.include_router(Tasks)