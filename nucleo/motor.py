class MotorIA:
    def __init__(self):
        self.nombre = "Leviatan"
        self.activo = True
    def procesar(self, mensaje):
        return f"[{self.nombre}] {mensaje}"
