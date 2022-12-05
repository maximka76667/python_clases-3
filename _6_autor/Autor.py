from _datetime import datetime


class Autor:

    def __init__(self, nombre, apellidos):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__ano_nacimiento = datetime.today().year
        self.__pais = ""

    # Nombre
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_apellidos(self):
        return self.__apellidos

    def set_apellidos(self, apellidos):
        self.__apellidos = apellidos

    def get_ano_nacimiento(self):
        return self.__ano_nacimiento

    def set_ano_nacimiento(self, ano_nacimiento):
        if ano_nacimiento > datetime.today().year:
            print("Anho nacimiento es superior al anho actual")
        else:
            self.__ano_nacimiento = ano_nacimiento

    def get_pais(self):
        return self.__pais

    def set_pais(self, pais):
        self.__pais = pais

    def ver_datos(self):
        print(self.__nombre, self.__apellidos, self.__ano_nacimiento, self.__pais, end = "")

    def get_edad(self):
        return datetime.today().year - self.__ano_nacimiento
