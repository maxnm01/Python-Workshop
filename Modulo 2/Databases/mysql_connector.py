# Importar bibliotecas
import mysql.connector as sql
import pandas as pd

# Crear conexión a la base de datos remota
db_connection = sql.connect(
    host='energia-rds.ce1ey5bjd9gj.us-east-2.rds.amazonaws.com', 
    database='sakila', 
    user='GUEST', 
    password='ATT.696.Guest')

# Consultar la tabla de actor de la base de datos de sakila
df = pd.read_sql('SELECT * FROM sakila.actor', con=db_connection)

# Visualizar los primeros 5 registros de la base de datos
print(df)

# Cerrar la conexión a la base de datos
db_connection.close()
