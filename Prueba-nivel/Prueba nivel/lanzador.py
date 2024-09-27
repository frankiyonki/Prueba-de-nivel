def main():
  """
  Función principal que crea una lista de vehículos y los imprime. 
  Posteriormente, cataloga la lista de vehículos con una función aparte.
  """
  vehiculos = []

  # Se crea un coche de color rojo, con 4 ruedas, velocidad máxima de 180 km/h y cilindrada de 1600 cc
  vehiculo1 = Coche("Rojo", 4, 180, 1600)  # color, ruedas, velocidad, cilindrada
  vehiculos.append(vehiculo1)
  print(vehiculo1)

  # Se crea una bicicleta de color verde, con 2 ruedas y de tipo montaña
  vehiculo2 = Bicicleta("Verde", 2, "Montaña")  # color, ruedas, tipo
  vehiculos.append(vehiculo2)
  print(vehiculo2)

  # Se crea una motocicleta de color gris, con 2 ruedas, tipo chopper, velocidad máxima de 200 km/h y cilindrada de 1200 cc
  vehiculo3 = Motocicleta("Gris", 2, "Chopper", 200, 1200)  # color, ruedas, tipo, velocidad, cilindrada
  vehiculos.append(vehiculo3)
  print(vehiculo3)

  # Se crea una camioneta de color blanco, con 4 ruedas, velocidad máxima de 120 km/h, cilindrada de 3000 cc y capacidad de carga de 2000 kg
  vehiculo4 = Camioneta("Blanco", 4, 120, 3000, 2000)  # color, ruedas, velocidad, cilindrada, carga
  vehiculos.append(vehiculo4)
  print(vehiculo4)

  # Se cataloga la lista de vehículos creada
  catalogar(vehiculos)