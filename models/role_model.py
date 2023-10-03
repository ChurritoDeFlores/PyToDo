#Imports
from pydantic import BaseModel
## Clase
class Role(BaseModel):
    id: int | None = None
    name: str | None = None
    status: str | None = None ## Activo / Inactivo