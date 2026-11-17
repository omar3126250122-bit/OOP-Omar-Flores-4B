# Excepción base del sistema; las demás heredan de ella
class ErrorInventario(Exception):
    pass

class ProductoNoEncontrado(ErrorInventario):
    pass

class CantidadInvalida(ErrorInventario):
    pass

class StockInsuficiente(ErrorInventario):
    pass