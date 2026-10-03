class Memoria:
    def __init__(self):
        self.historial = []
    def guardar(self, e, s):
        self.historial.append({"e":e,"s":s})
