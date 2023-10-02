## Imports
from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: int| None = None
    name: str
    password: str
    role: int | None = 2 ## 1 : Administrador // 2 : Usuario 
    status: int | None = 1 ## 1: Activo // 2: Inactivo
    created_at: datetime | None = datetime.now()
