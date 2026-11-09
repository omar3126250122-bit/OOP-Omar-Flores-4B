import csv
import json
from abc import ABC, abstractmethod
from datetime import datetime
from decimal import Decimal
from fpdf import FPDF


class Exportador(ABC):
    """Clase base abstracta: define el contrato que cumplen todas las hijas."""

    # Cada hija sobrescribe estos datos (los usa el Controlador/Vista para
    # el cuadro de "Guardar como", sin tener que conocer el formato).
    NOMBRE = ""
    EXTENSION = ""

    COLUMNAS = ("ID", "Nombre", "Precio", "Stock")
    _CLAVES = ("id", "nombre", "precio", "stock")

    @abstractmethod
    def export(self, datos, ruta_archivo):
        """Método que debe ser sobrescrito por las clases hijas."""
        raise NotImplementedError(
            "Este método debe ser implementado por la subclase."
        )

    def exportar(self, datos, ruta_archivo):
        """Alias en español de export() (nombre usado en la guía)."""
        return self.export(datos, ruta_archivo)

    # ---- utilidades compartidas por las hijas -------------------------
    @classmethod
    def _fila(cls, producto):
        """Convierte una tupla o diccionario en una lista [id, nombre, precio, stock]."""
        if isinstance(producto, dict):
            return [producto.get(clave) for clave in cls._CLAVES]
        return list(producto)

    @staticmethod
    def _numero(valor):
        """Decimal (lo que devuelve MySQL) -> float, para que json lo acepte."""
        if isinstance(valor, Decimal):
            return float(valor)
        return valor

    @classmethod
    def _precio(cls, valor):
        """Precio con dos decimales: 12.5 -> '12.50'."""
        try:
            return f"{float(cls._numero(valor)):.2f}"
        except (TypeError, ValueError):
            return str(valor)


class ExportadorCSV(Exportador):
    NOMBRE = "CSV"
    EXTENSION = ".csv"

    def export(self, datos, ruta_archivo):
        # utf-8-sig para que Excel muestre bien los acentos; newline=''
        # evita líneas en blanco extra en Windows.
        with open(ruta_archivo, "w", newline="", encoding="utf-8-sig") as file:
            escritor = csv.writer(file)
            escritor.writerow(self.COLUMNAS)
            for producto in datos:
                id_, nombre, precio, stock = self._fila(producto)
                escritor.writerow([id_, nombre, self._precio(precio), stock])
        print(f"Archivo CSV generado en: {ruta_archivo}")


class ExportadorTXT(Exportador):
    NOMBRE = "TXT"
    EXTENSION = ".txt"

    def export(self, datos, ruta_archivo):
        with open(ruta_archivo, "w", encoding="utf-8") as file:
            file.write("--- REPORTE DE PRODUCTOS ---\n")
            for producto in datos:
                id_, nombre, precio, stock = self._fila(producto)
                file.write(
                    f"ID: {id_} | Nombre: {nombre} | "
                    f"Precio: ${self._precio(precio)} | Stock: {stock}\n"
                )
        print(f"Archivo TXT generado en: {ruta_archivo}")


class ExportadorJSON(Exportador):
    NOMBRE = "JSON"
    EXTENSION = ".json"

    def export(self, datos, ruta_archivo):
        productos = []
        for producto in datos:
            fila = [self._numero(valor) for valor in self._fila(producto)]
            productos.append(dict(zip(self._CLAVES, fila)))

        with open(ruta_archivo, "w", encoding="utf-8") as file:
            json.dump(productos, file, ensure_ascii=False, indent=4)
        print(f"Archivo JSON generado en: {ruta_archivo}")


class ExportadorPDF(Exportador):
    NOMBRE = "PDF"
    EXTENSION = ".pdf"

    # Ancho de cada columna (mm): ID, Nombre, Precio, Stock.
    _ANCHOS = (20, 90, 40, 30)
    _ALTO_FILA = 8
    _LIMITE_Y = 265  # a partir de aquí se abre una página nueva

    @staticmethod
    def _texto(valor, maximo=None):
        """Las fuentes base de FPDF solo admiten latin-1; se evita que falle."""
        texto = str(valor)
        if maximo is not None and len(texto) > maximo:
            texto = texto[: maximo - 3] + "..."
        return texto.encode("latin-1", "replace").decode("latin-1")

    def _encabezado_tabla(self, pdf):
        pdf.set_font("Arial", "B", 11)
        pdf.set_fill_color(220, 220, 220)
        for ancho, titulo in zip(self._ANCHOS, self.COLUMNAS):
            pdf.cell(ancho, self._ALTO_FILA, titulo, border=1, align="C", fill=True)
        pdf.ln(self._ALTO_FILA)
        pdf.set_font("Arial", size=11)

    def export(self, datos, ruta_archivo):
        if FPDF is None:
            raise RuntimeError(
                "La librería fpdf no está instalada. "
                "Ejecuta: pip install fpdf"
            )

        pdf = FPDF()
        pdf.add_page()

        # Configuración del título
        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, "Reporte de Inventario de Productos", align="C")
        pdf.ln(10)

        pdf.set_font("Arial", size=10)
        fecha = datetime.now().strftime("%d/%m/%Y %H:%M")
        pdf.cell(0, 8, f"Generado: {fecha}", align="C")

        # Salto de línea
        pdf.ln(12)

        # Cuerpo del documento (tabla)
        self._encabezado_tabla(pdf)

        total = 0
        for producto in datos:
            if pdf.get_y() > self._LIMITE_Y:
                pdf.add_page()
                self._encabezado_tabla(pdf)

            id_, nombre, precio, stock = self._fila(producto)
            celdas = (
                self._texto(id_),
                self._texto(nombre, 42),
                self._texto("$" + self._precio(precio)),
                self._texto(stock),
            )
            alineaciones = ("C", "L", "R", "C")
            for ancho, texto, alineacion in zip(self._ANCHOS, celdas, alineaciones):
                pdf.cell(ancho, self._ALTO_FILA, texto, border=1, align=alineacion)
            pdf.ln(self._ALTO_FILA)
            total += 1

        pdf.ln(4)
        pdf.set_font("Arial", "B", 11)
        pdf.cell(0, 8, f"Total de productos: {total}")

        pdf.output(ruta_archivo)
        print(f"Archivo PDF generado en: {ruta_archivo}")
