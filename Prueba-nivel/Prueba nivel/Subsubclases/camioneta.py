from subclase.coche import Coche

class Camioneta(Vehiculo):
    def __init__(self, color, ruedas, carga):
        super().__init__(color, ruedas)
        self.carga = carga
    
    def __str__(self):
        return f"Camioneta: {super().__str__()}, Carga: {self.carga} kg"
    
    def cargar(self):
        print("La camioneta está cargada")
    
    def descargar(self):
        print("La camioneta está descargada")