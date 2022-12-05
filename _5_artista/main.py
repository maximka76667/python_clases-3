from _5_artista.Artista import Artista
from _5_artista.Disco import Disco
artista = Artista("Shakira", "Colombia", 1977)

artista.show_info()
print()

disco = Disco("Sale el sol", artista)
disco.set_ano_lanzamiento(2009)
disco.set_num_canciones(15)

disco.ver_datos()
