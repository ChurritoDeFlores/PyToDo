## Import
from fastapi import FastAPI
from routes.user_route import Users
from routes.role_route import Roles
from routes.task_route import Tasks
from starlette.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import os
## punto de arranque (uvicorn index:index) --reload [para tener que ejecutar el comando cada vez que se realize un cambio]
index = FastAPI()

# Configuracion opciones CORS
origins = [
    "http://localhost:3000",  # Origen de front
    # Puedes agregar más orígenes si es necesario
]

index.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
)

@index.get('/', response_class=HTMLResponse)
def getRoot():
    with open(os.path.join(os.path.dirname(__file__), 'template/index.html'), 'r') as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

## Incluir las rutas que vienen de el archivo user.py
index.include_router(Users)
index.include_router(Roles)
index.include_router(Tasks)