from _datetime import datetime
from _functools import reduce


def return_jugador_maximo(jugador_maximo, jugador):
    if jugador.get_media() > jugador_maximo.get_media():
        return jugador
    return jugador_maximo


class Equipo_baloncesto:

    def __init__(self, nombre):
        self.__nombre = nombre
        self.__fecha_fundacion = None
        self.__jugadores = []

    def get_nombre(self):
        return self.__nombre

    def get_fecha_fundacion(self):
        return self.__fecha_fundacion

    def get_jugadores(self):
        return self.__jugadores

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_fecha_fundacion(self, fecha_fundacion):
        if fecha_fundacion > datetime.today():
            print("error")
        else:
            self.__fecha_fundacion = fecha_fundacion
            
    def set_jugadores(self, jugadores):
        self.__jugadores = jugadores
                
    def get_anotador_maximo(self):
        return reduce(return_jugador_maximo, self.__jugadores)

    def ver_datos(self):
        print(self.__nombre, self.__fecha_fundacion)
        for jugador in self.__jugadores:
            jugador.ver_datos()

    def setJugador1(self, jugador1):
        self.__jugadores.append(jugador1)

    def setJugador2(self, jugador2):
        self.__jugadores.append(jugador2)

    def setJugador3(self, jugador3):
        self.__jugadores.append(jugador3)

    def setJugador4(self, jugador4):
        self.__jugadores.append(jugador4)

    def setJugador5(self, jugador5):
        self.__jugadores.append(jugador5)
