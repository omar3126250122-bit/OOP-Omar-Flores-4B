from Controllers import conexion_controller
import mysql.connector


class ProductModel:

    def __init__(self):
        self.conexion_db = conexion_controller.Conexion()
        self._asegurar_tabla()

    def _asegurar_tabla(self):
        # Crea la tabla si todavía no existe (ver también schema.sql).
        conexion = self.conexion_db.conectar()

        if conexion is None:
            return

        cursor = None

        try:
            cursor = conexion.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS productos (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(100) NOT NULL,
                    precio DECIMAL(10, 2) NOT NULL,
                    stock INT NOT NULL DEFAULT 0
                )
            """)
            conexion.commit()

        except mysql.connector.Error as error:
            print("Error al crear la tabla productos:", error)

        finally:
            if cursor is not None:
                cursor.close()
            conexion.close()

    def registrar_producto(self, nombre, precio, stock):
        conexion = self.conexion_db.conectar()

        if conexion is None:
            return "error"

        cursor = None

        try:
            cursor = conexion.cursor()

            consulta = """
                INSERT INTO productos (nombre, precio, stock)
                VALUES (%s, %s, %s)
            """

            cursor.execute(consulta, (nombre, precio, stock))
            conexion.commit()

            return "ok"

        except mysql.connector.Error as error:
            print("Error al registrar producto:", error)
            return "error"

        finally:
            if cursor is not None:
                cursor.close()
            conexion.close()

    def obtener_productos(self):
        conexion = self.conexion_db.conectar()

        if conexion is None:
            return None

        cursor = None

        try:
            cursor = conexion.cursor()

            cursor.execute(
                "SELECT id, nombre, precio, stock FROM productos ORDER BY id"
            )

            return cursor.fetchall()

        except mysql.connector.Error as error:
            print("Error al obtener productos:", error)
            return None

        finally:
            if cursor is not None:
                cursor.close()
            conexion.close()
