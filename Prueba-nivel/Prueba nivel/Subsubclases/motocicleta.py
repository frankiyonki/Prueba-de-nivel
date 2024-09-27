from subclases.bicicleta import Bicicleta 

class Motocicleta(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"Motocicleta de color {self.color}, con {self.ruedas} ruedas, velocidad {self.velocidad} y cilindrada {self.cilindrada}"

    def acelerar(self):
        """
        Acelera la motocicleta.
        """
        self.velocidad += 10

    def frenar(self):
        """
        Frena la motocicleta.
        """
        self.velocidad -= 10



