class Jugador:
    
    def __init__(self,nombre,apellidos,dorsal,media):
        self.__nombre=nombre
        self.__apellidos=apellidos
        self.__dorsal=dorsal
        if media>=0:
            self.__media=media
        else:
            print("ERRO")

    def setMedia(self,media):
        if media>=0:
            self.__media=media
        else:
            print("ERRO")

    def ver_datos(self):
        print(self.__nombre)

class Equipo_baloncesto:
    def __init__(self,nombre):
        self.__nombre=nombre
        self.__fechaFundacion=None
        self.__jugador1=None
        self.__jugador2=None
        self.__jugador3=None
        self.__jugador4=None
        self.__jugador5=None
    
    def ver_datos(self):
        print(self.__nombre,self.__fechaFundacion)
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
            self.__jugado3.ver_datos()
        if (self.__jugador4 is None):
            print("No hay jugador 4")
        else:
            self.__jugador4.ver_datos()
        if (self.__jugador5 is None):
            print("No hay jugador 5")
        else:
            self.__jugador5.ver_datos()
     
    def setJugador1(self,jugador1):
        self.__jugador1=jugador1
    
    def setJugador2(self,jugador2):
        self.__jugador2=jugador2
    
    def setJugador3(self,jugador3):
        self.__jugador3=jugador3
    
    def setJugador4(self,jugador4):
        self.__jugador4=jugador4
    
    def setJugador5(self,jugador5):
        self.__jugador5=jugador5
        
    
        
        
jugador1 = Jugador("Pepito","Perez",1,14)
equipo1 = Equipo_baloncesto("Equipo 1")
equipo1.setJugador1(jugador1)
equipo1.ver_datos()