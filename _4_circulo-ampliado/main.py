from _2_punto.Punto import Punto
from Circulo import Circulo

circulo = Circulo(Punto(20, 30), 6)

print(circulo.calcular_longitud_circunferencia())

circulo.desplazar_x(10)

circulo.show_info()

circulo.set_radio(7.5)

circulo.show_info()
