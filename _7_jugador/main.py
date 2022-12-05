from _7_jugador.Equipo_baloncesto_a import Equipo_baloncesto
# from _7_jugador.Equipo_baloncesto_b import Equipo_baloncesto

from _7_jugador.Jugador import Jugador

jugador1 = Jugador("Pepito1", "Perez", 1, 14)
jugador2 = Jugador("Pepito2", "Perez", 2, 10)
jugador3 = Jugador("Pepito3", "Perez", 3, 15)
jugador4 = Jugador("Pepito4", "Perez", 4, 8)
jugador5 = Jugador("Pepito5", "Perez", 5, 10)

equipo = Equipo_baloncesto("Equipo 1")

equipo.setJugador1(jugador1)
equipo.setJugador2(jugador2)
equipo.setJugador3(jugador3)
equipo.setJugador4(jugador4)
equipo.setJugador5(jugador5)
equipo.ver_datos()

print("Anotador maximo: ")
equipo.get_anotador_maximo().ver_datos()
