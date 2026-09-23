class Producto:
    def __init__(self, nombre, precio, tipo):
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo


class ProductoElectronico(Producto):
    def __init__(self,nombre,precio,tipo,marca,garantia,estado_fisico):
        super().__init__(nombre,precio,tipo)
        self.marca = marca
        self.garantia = garantia
        self.estado = estado_fisico

    def reparar(self):
        if self.estado == "mal estado":
            print(f"{self.nombre} está en mal estado, se va a reparar")
            self.estado = "reparado"
        else:
            print(f"{self.nombre} esta en buen estado.")

class ProductoDeRopa(Producto):
    def __init__(self,nombre,precio,tipo,talla,color):
        super().__init__(nombre,precio,tipo)
        self.talla = talla
        self.color = color

    def Medir_Ropa(self):
        print(f"Te puedes probar la prenda {self.nombre} de talla {self.talla}")

class ProductoAlimenticio(Producto):
    def __init__(self,nombre,precio,tipo,fecha_caducidad,calorias):
        super().__init__(nombre,precio,tipo)
        self.caducidad = fecha_caducidad
        self.calorias = calorias
    def congelar(self, tiempo_dias):
        print(f"Se ha extendido la fecha de caducidad {tiempo_dias} dias")
        


class Pedido:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.productos = []
        self.estado = "CREADO"

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_total(self):
        total = 0

        for producto in self.productos:

            if producto.tipo == "electronico":
                total += producto.precio * 1.16

            elif producto.tipo == "ropa":
                total += producto.precio * 1.08

            elif producto.tipo == "alimento":
                total += producto.precio * 1.00

        return total

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def mostrar_pedido(self):
        print(f"\nPedido #{self.numero}")
        print(f"Cliente: {self.cliente}")
        print(f"Estado: {self.estado}")

        print("\nProductos:")

        for producto in self.productos:
            print(
                f"- {producto.nombre}: "
                f"${producto.precio:.2f}"
            )

        print(f"\nTotal: ${self.calcular_total():.2f}")


# main program

pedido = Pedido(1001, "Ana")

pedido.agregar_producto(
    ProductoElectronico("Laptop", 15000, "electronico","Asus","1 año de garantia","Impecable")
)

pedido.agregar_producto(
    ProductoDeRopa("Playera", 500, "ropa","Media","Rojo")
)

pedido.agregar_producto(
    ProductoAlimenticio("Carne", 140, "alimento","30/10/2026",230)
)

pedido.mostrar_pedido()

pedido.cambiar_estado("ENVIADO")

print("\nNuevo estado:", pedido.estado)