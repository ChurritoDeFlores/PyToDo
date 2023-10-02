# PyToDo
Este sera una pequeña API, hecha con FastAPI y PHPMySQL
Uso entornos virtuales "venv"
Uso el paquete XAMPP donde despliego mi base de datos
El objetivo de la aplicacion es realizar una agenda, que contenga usuarios y las tareas que desean registrar.
Tablas:
  Users
  - id (int) PK
  - name (str) not null 
  - password (str) not null
  - role_id (int) not null default(2=Usuario)
  - status (int) not null default(1=Activo)
  - created_at (datetime) not null default(datetime.now)
  Roles
  - id (int) PK
  - name (str) not null
  Tasks
  - id (int) PK
  - text (str) not null
  - user_id (int) not null
  - crated_at (datetime) not null default(datetime.now)
  - completed_at (datetime) null
