from math import pow

class Circulo:
    PI = 3.14159
    
    def __init__(self, punto, radio):
        self.__punto = punto
        self.__radio = radio
        
    def calcular_area(self):
        return self.PI * pow(self.__radio, 2)
    
    def calcular_longitud_circunferencia(self):
        return 2 * self.PI * self.__radio
    
    def desplazar_x(self, x):
        self.__punto.desplazar_x(x)
        
    def desplazar_y(self, y):
        self.__punto.desplazar_y(y)
        
    def show_info(self):
        print("Circulo(", end='')
        self.__punto.show_info()
        print(", " + str(self.__radio) + ")")
        
    def set_radio(self, radio):
        self.__radio = radio
