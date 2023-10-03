##Imports
from sqlalchemy import Table, Column
from sqlalchemy import Integer,String
from config.db import meta, engine
#Tabla
roles = Table("roles", meta,Column("id",Integer,primary_key=True),Column("name",String(255)),Column("status",String(255)))

meta.create_all(engine)