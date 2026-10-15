import psycopg2
from psycopg2 import Error
from .config import DB_config
import psycopg2.extras


class Database_connection:

  def __init__(self):
    self.config = DB_config

  def obtener_conexion(self):
    try:
      # AQUÍ ESTABA EL ERROR: se quitó '.connector'
      conexion = psycopg2.connect(**self.config)
      return conexion
    except Error as e:
      print(f'Error al conectar con PostgreSQL: {e}')
      return None

  def ejecutar_consulta(self, query, params=()):
    conexion = self.obtener_conexion()
    if not conexion:
      return None

    cursor = conexion.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    try:
      cursor.execute(query, params)

      if query.strip().upper().startswith('SELECT'):
        resultados = cursor.fetchall()
        return resultados
      else:
        conexion.commit()
        return cursor.rowcount
    except Error as e:
      print(f'Error en la consulta SQL: {e}')
      return None
    finally:
      if conexion:
        cursor.close()
        conexion.close()