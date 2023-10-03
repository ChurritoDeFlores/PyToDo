## Imports
from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
    id: int | None = None
    name: str | None = None
    password: str | None = None
    role: int | None = None ## 1 : Administrador // 2 : Usuario 
    status: str | None = None ## Activo / Inactivo
    created_at: datetime | None = None
