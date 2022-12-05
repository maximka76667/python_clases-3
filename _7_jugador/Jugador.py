class Jugador:

    def __init__(self, nombre, apellidos, dorsal, media):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__dorsal = dorsal
        self.set_media(media)

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_apellidos(self):
        return self.__apellidos

    def set_apellidos(self, apellidos):
        self.__apellidos = apellidos

    def get_dorsal(self):
        return self.__dorsal

    def set_dorsal(self, dorsal):
        if dorsal < 0 or dorsal > 100:
            print("Error")
        else:
            self.__dorsal = dorsal

    def get_media(self):
        return self.__media

    def set_media(self, media):
        if media >= 0:
            self.__media = media
        else:
            print("ERRO")

    def ver_datos(self):
        print(self.__nombre, self.__apellidos, self.__dorsal, self.__media)
