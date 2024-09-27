from superclases.vehiculo import Vehiculo 

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f"Bicicleta {self.tipo}, color {self.color}, con {self.ruedas} ruedas"

    def inflar_ruedas(self):
        print("Las ruedas de la bicicleta se están inflando...")

    def cambiar_cadena(self):
        print("La cadena de la bicicleta se ha cambiado.")