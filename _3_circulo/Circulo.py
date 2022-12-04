from math import pow
class Circulo:
    PI = 3.14159
    
    def __init__(self, punto, radio):
        self.__punto = punto
        self.__radio = radio
        
    def calcular_area(self):
        return self.PI * pow(self.__radio, 2)