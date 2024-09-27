from superclases.vehiculo import Vehiculo 

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"Coche: {super().__str__()}, velocidad: {self.velocidad}, cilindrada: {self.cilindrada}"
        
    def acelerar(self, incremento):
        self.velocidad += incremento

    def frenar(self, decremento):
        self.velocidad -= decremento

    def arrancar(self):
        print("El coche ha arrancado")

    def parar(self):
        print("El coche se ha parado")