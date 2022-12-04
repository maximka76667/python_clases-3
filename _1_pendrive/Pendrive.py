class Pendrive:
    iva = 0.18
    
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo
        
    def getPrecioIva(self):
        return self.precio * (1 + self.iva)
