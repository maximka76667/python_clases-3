from datetime import datetime
class Artista:
    def __init__(self, nombre, pais, ano_nacimiento):
        self.__nombre = nombre
        self.__pais = pais
        self.__ano_nacimiento = ano_nacimiento
        
    def get_nombre(self):
        return self.__nombre
    
    def get_pais(self):
        return self.__pais
    
    def get_ano_nacimiento(self):
        return self.__ano_nacimiento
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def set_pais(self, pais):
        self.__pais = pais
        
    def set_ano_nacimiento(self, ano_nacimiento):
        self.__ano_nacimiento = ano_nacimiento
        
    def get_edad(self):
        return datetime.today().year - self.__ano_nacimiento
        