class SuscripcionExpiradaError(Exception):
    pass

class PuntosInsuficientesError(Exception):
    pass

class PerfilMovil:
    def __init__(self, username: str, gemas: int = 50,racha_dias: int = 1, notificaciones_activas: bool = True):
        if gemas < 0:
            raise ValueError("Las gemas no pueden ser negativas")
        self.username = username
        self.gemas = gemas
        self.racha_dias = racha_dias
        self.notificaciones_activas = notificaciones_activas

    def ganar_gemas(self, cantidad: int) -> int:
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser estrictamente positiva")
        self.gemas += cantidad
        return self.gemas

    def gastar_gemas(self, cantidad: int) -> int:
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser estrictamente positiva")
        if cantidad > self.gemas:
            raise PuntosInsuficientesError(
                f"Tienes {self.gemas} gemas y quieres gastar {cantidad}")
        self.gemas -= cantidad
        return self.gemas

class PerfilPro(PerfilMovil):
    def __init__(self, username: str, meses_suscripcion: int, **kwargs):
        if meses_suscripcion <= 0:
            raise ValueError("Los meses de suscripción deben ser mayores a 0")
        super().__init__(username, **kwargs)  # reutiliza el __init__ del padre
        self.meses_suscripcion = meses_suscripcion
        self.es_pro = True

    def descargar_contenido_offline(self) -> str:
        if self.meses_suscripcion <= 0:
            self.es_pro = False
            raise SuscripcionExpiradaError("Tu suscripción Pro ha expirado")
        return "Descarga offline completada"