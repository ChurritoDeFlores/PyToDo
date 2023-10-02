from sqlalchemy import create_engine, MetaData
## Conexion
engine = create_engine("mysql+pymysql://root:@localhost:3306/api_todo")
## MetaData
meta = MetaData()
## Objeto de conexion
# cnn = engine.connect() ## No lo uso, ya que hace que la conexion permanezca abierta