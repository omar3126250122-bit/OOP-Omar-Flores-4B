import exceptions

class Producto:
    def __init__(self, codigo, stock):
        self.codigo = codigo
        self.stock = stock

    def retirar(self, cantidad):
        # Validacion 1: debe ser entero y mayor que cero
        # raise lanza la excepcion y detiene la ejecucion del metodo
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise exceptions.CantidadInvalida("La cantidad debe ser un entero positivo")
        # Validacion 2: stock suficiente
        if cantidad > self.stock:
            raise exceptions.StockInsuficiente(
                f"Stock insuficiente. Disponible: {self.stock}")
        # Si todo es valido, se descuenta y se devuelve el stock restante
        self.stock -= cantidad
        return self.stock