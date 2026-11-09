from decimal import Decimal, InvalidOperation

from Views import Products_view

# Solo se importan las CLASES del módulo de exportación.
# Aquí no hay (ni debe haber) imports de csv, json ni fpdf.
from Models.exporters import (
    ExportadorCSV,
    ExportadorTXT,
    ExportadorJSON,
    ExportadorPDF,
)


class ProductsController:
    # Formato elegido en el Combobox -> clase que sabe generarlo.
    # Es un diccionario (no una cadena de if/elif): agregar un formato nuevo
    # es agregar una clase hija y una línea aquí.
    EXPORTADORES = {
        "CSV": ExportadorCSV,
        "TXT": ExportadorTXT,
        "JSON": ExportadorJSON,
        "PDF": ExportadorPDF,
    }

    def __init__(self, modelo, root):
        self.modelo = modelo
        self.root = root
        self.vista = None

    # ---------- Ventana ----------
    def abrir(self, nombre_usuario=""):
        if self.vista is not None and self.vista.ventana.winfo_exists():
            self.vista.ventana.lift()
            self.vista.ventana.focus_force()
            return

        # Oculta el login mientras se usa el inventario.
        self.root.withdraw()

        self.vista = Products_view.ProductsView(self.root, nombre_usuario)

        self.vista.btn_guardar.config(
            command=self.registrar_producto
        )

        # El botón le pasa al controlador el formato elegido en el Combobox.
        self.vista.btn_exportar.config(
            command=lambda: self.generar_reporte(self.vista.obtener_formato())
        )

        self.vista.ventana.protocol(
            "WM_DELETE_WINDOW",
            self.cerrar
        )

        self.cargar_productos()

    def cerrar(self):
        if self.vista is not None:
            if self.vista.ventana.winfo_exists():
                self.vista.cerrar()

            self.vista = None

        # Regresa a la pantalla de login.
        self.root.deiconify()

    # ---------- Productos ----------
    def cargar_productos(self):
        productos = self.modelo.obtener_productos()

        if productos is None:
            self.vista.mostrar_mensaje(
                "Error",
                "No fue posible consultar los productos. "
                "Verifica la conexión con MySQL.",
                "error"
            )
            return

        self.vista.cargar_tabla(productos)

    def registrar_producto(self):
        nombre, precio_txt, stock_txt = self.vista.obtener_datos()

        if not nombre or not precio_txt or not stock_txt:
            self.vista.mostrar_mensaje(
                "Campos vacíos",
                "Nombre, precio y stock son obligatorios.",
                "error"
            )
            return

        try:
            precio = Decimal(precio_txt.replace(",", "."))
            if not precio.is_finite() or precio < 0:
                raise InvalidOperation
        except InvalidOperation:
            self.vista.mostrar_mensaje(
                "Precio inválido",
                "El precio debe ser un número mayor o igual a 0.",
                "error"
            )
            return

        try:
            stock = int(stock_txt)
            if stock < 0:
                raise ValueError
        except ValueError:
            self.vista.mostrar_mensaje(
                "Stock inválido",
                "El stock debe ser un número entero mayor o igual a 0.",
                "error"
            )
            return

        resultado = self.modelo.registrar_producto(nombre, precio, stock)

        if resultado == "ok":
            self.vista.limpiar_campos()
            self.cargar_productos()
        else:
            self.vista.mostrar_mensaje(
                "Error",
                "No fue posible registrar el producto. "
                "Verifica la conexión con MySQL.",
                "error"
            )

    # ---------- Exportación (polimorfismo) ----------
    def generar_reporte(self, formato):
        clase_exportador = self.EXPORTADORES.get(formato)

        if clase_exportador is None:
            self.vista.mostrar_mensaje(
                "Formato inválido",
                "Selecciona un formato de la lista.",
                "error"
            )
            return

        # 1. Datos reales desde el Modelo.
        productos = self.modelo.obtener_productos()

        if productos is None:
            self.vista.mostrar_mensaje(
                "Error",
                "No fue posible consultar los productos. "
                "Verifica la conexión con MySQL.",
                "error"
            )
            return

        if not productos:
            self.vista.mostrar_mensaje(
                "Sin datos",
                "No hay productos registrados para exportar."
            )
            return

        # 2. Dónde guardar (cuadro de diálogo de la Vista).
        ruta = self.vista.pedir_ruta_guardado(
            formato,
            clase_exportador.EXTENSION
        )

        if not ruta:
            return  # El usuario canceló.

        # 3. Se instancia SOLO la clase del formato elegido y se llama
        #    .export(). Al controlador no le importa cuál es.
        exportador = clase_exportador()

        try:
            exportador.export(productos, ruta)
        except Exception as error:
            self.vista.mostrar_mensaje(
                "Error al exportar",
                f"No se pudo generar el archivo {formato}.\n\n{error}",
                "error"
            )
            return

        self.vista.mostrar_mensaje(
            "Exportación exitosa",
            f"Se exportaron {len(productos)} productos.\n\n{ruta}"
        )
