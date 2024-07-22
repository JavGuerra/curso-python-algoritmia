# Importa el módulo que hace us ode SQLite
import sqlite3

# Abre la conexión
conexion = sqlite3.connect('ejemplo.sqlite')
# Establece el acceso a los datos
cursor = conexion.cursor()

# Consulta SQL
cursor.execute("SELECT * FROM Producto")
# Obtiene la lista de los datos
result = cursor.fetchall()
# Recorre los resultados
for x in result:
    print(f"id: {x[0]} producto: {x[1]} cantidad: {x[2]}")

# Importante: cerrar siempre la conexión
conexion.close()
