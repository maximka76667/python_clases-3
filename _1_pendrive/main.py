from _1_pendrive.Pendrive import Pendrive

marca = input("Marca: ")
modelo = input("Modelo: ")
precio = float(input("Precio: "))
capacidad = float(input("Capacidad: "))

pendrive = Pendrive(marca, modelo)
pendrive.precio = precio
pendrive.capacidad = capacidad

print(vars(pendrive))
print(pendrive.getPrecioIva())