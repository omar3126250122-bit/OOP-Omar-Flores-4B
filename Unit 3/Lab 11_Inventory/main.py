import exceptions
from inventory import Inventario

def main():
    inventario = Inventario()
    try:
        # try: codigo que puede generar errores
        codigo = input("Codigo del producto: ")
        cantidad = int(input("Cantidad a retirar: "))  # ValueError si no es entero
        restante = inventario.retirar(codigo, cantidad)
    except ValueError:
        # Se ejecuta si el usuario escribe texto en vez de un numero
        print("La cantidad debe ser un número entero.")
    except exceptions.ErrorInventario as error:
        # Captura ProductoNoEncontrado, CantidadInvalida y StockInsuficiente
        print(f"No se puede realizar la operación: {error}")
    else:
        # else: solo se ejecuta si no hubo ninguna excepcion
        print(f"Retiro realizado con éxito. Stock restante: {restante}")

if __name__ == "__main__":
    main()