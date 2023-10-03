from sqlalchemy import create_engine, MetaData
## Conexion (Es necesario cambiar los datos del stringconnection si se instala)
# user:'root'
# password:''
# server:'localhost'
# port:3306
# db:'api_todo'
engine = create_engine("mysql+pymysql://root:@localhost:3306/api_todo")
## MetaData
meta = MetaData()
## Objeto de conexion
# cnn = engine.connect() ## No lo uso, ya que hace que la conexion permanezca abierta