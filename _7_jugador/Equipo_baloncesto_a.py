class Equipo_baloncesto:

    def __init__(self, nombre):
        self.__nombre = nombre
        self.__fechaFundacion = None
        self.__jugador1 = None
        self.__jugador2 = None
        self.__jugador3 = None
        self.__jugador4 = None
        self.__jugador5 = None

    def ver_datos(self):
        print(self.__nombre, self.__fechaFundacion)
        if (self.__jugador1 is None):
            print("No hay jugador 1")
        else:
            self.__jugador1.ver_datos()
        if (self.__jugador2 is None):
            print("No hay jugador 2")
        else:
            self.__jugador2.ver_datos()
        if (self.__jugador3 is None):
            print("No hay jugador 3")
        else:
            self.__jugador3.ver_datos()
        if (self.__jugador4 is None):
            print("No hay jugador 4")
        else:
            self.__jugador4.ver_datos()
        if (self.__jugador5 is None):
            print("No hay jugador 5")
        else:
            self.__jugador5.ver_datos()
            
    def get_anotador_maximo(self):
        jugador_maximo = self.__jugador1
        if jugador_maximo.get_media() < self.__jugador2.get_media():
            jugador_maximo = self.__jugador2
            
        if jugador_maximo.get_media() < self.__jugador3.get_media():
            jugador_maximo = self.__jugador3

        if jugador_maximo.get_media() < self.__jugador4.get_media():
            jugador_maximo = self.__jugador4

        if jugador_maximo.get_media() < self.__jugador5.get_media():
            jugador_maximo = self.__jugador5

        return jugador_maximo

    def setJugador1(self, jugador1):
        self.__jugador1 = jugador1

    def setJugador2(self, jugador2):
        self.__jugador2 = jugador2

    def setJugador3(self, jugador3):
        self.__jugador3 = jugador3

    def setJugador4(self, jugador4):
        self.__jugador4 = jugador4

    def setJugador5(self, jugador5):
        self.__jugador5 = jugador5
