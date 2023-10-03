## Imports
from datetime import datetime
from pydantic import BaseModel
##Clases
class Task(BaseModel):
    id: int | None=None 
    text: str | None=None 
    user_id: int | None=None 
    created_at: datetime | None=None 
    completed_at: datetime | None=None 