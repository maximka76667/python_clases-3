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
        self.__jugadores=[]
    
    def ver_datos(self):
        print(self.__nombre,self.__fechaFundacion)
        for jugador in self.__jugadores:
            jugador.ver_datos()
     
    def setJugador1(self,jugador1):
        self.__jugadores.append(jugador1)
    
    def setJugador2(self,jugador2):
        self.__jugadores.append(jugador2)
    
    def setJugador3(self,jugador3):
        self.__jugadores.append(jugador3)
    
    def setJugador4(self,jugador4):
        self.__jugadores.append(jugador4)
    
    def setJugador5(self,jugador5):
        self.__jugadores.append(jugador5)
        
        
jugador1 = Jugador("Pepito","Perez",1,14)
equipo1 = Equipo_baloncesto("Equipo 1")
equipo1.setJugador1(jugador1)
equipo1.ver_datos()