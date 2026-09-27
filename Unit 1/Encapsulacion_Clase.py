class Cuenta:
    def __init__(self, nombre, edad, dinero):
        
        self.nombre = nombre

        self._edad = edad

        self.__dinero = dinero

    def get_dinero(self):
        return self.__dinero

    def set_dinero(self, cantidad):
        self.__dinero += cantidad


cuenta1 = Cuenta("Omar", 19, 1000)

# # Atributo publico
print(cuenta1.nombre)

# Atributo protegido
print(cuenta1._edad)

# Atributo privado mediante un método
print(cuenta1.get_dinero())

# Modificar el atributo privado
cuenta1.set_dinero(1500)
print(cuenta1.get_dinero())
