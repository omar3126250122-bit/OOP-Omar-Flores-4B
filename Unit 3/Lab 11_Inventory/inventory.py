#Lab 11. Exception handling OOP
#A store needs to deduct products from its inventory.The system must prevent invalid operations and communicate errors appropiately, without terminating execution unexpectedly.

#Custom exceptions
from products import Producto
import exceptions

class Inventario:
    def __init__(self):
        self.productos = {
            "P01": Producto("P01", 5),
            "P02": Producto("P02", 10),
            "P03": Producto("P03", 20),
            "P04": Producto("P04", 40),
            "P05": Producto("P05", 80)
        }

    def retirar(self, codigo, cantidad):
        # Verifica que el producto exista
        if codigo not in self.productos:
            raise exceptions.ProductoNoEncontrado("El producto no existe")
        # Delega el descuento a Producto; sus excepciones se propagan a main
        return self.productos[codigo].retirar(cantidad)
        #Step 4: Verify that the product exists.
        #Step 5: Delegade the discount to the Product class. 
