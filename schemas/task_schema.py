##Imports
from sqlalchemy import Table, Column
from sqlalchemy import Integer,Text,DateTime
from config.db import meta, engine
#Tabla
tasks = Table("tasks", meta,
              Column("id",Integer,primary_key=True),
              Column("text",Text),
              Column("user_id",Integer),
              Column("created_at",DateTime),
              Column("completed_at",DateTime))

meta.create_all(engine)