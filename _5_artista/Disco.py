from _datetime import datetime
class Disco:

    # Titulo, artista, ano lanzamiento, numero canciones
    def __init__(self, titulo, artista):
        self.__titulo = titulo
        self.__artista = artista
        self.__ano_lanzamiento = datetime.today().year
        self.__num_canciones = 1

    # Titulo
    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    # Artista
    def get_artista(self):
        return self.__artista

    def set_artista(self, artista):
        self.__artista = artista

    # Ano lanzamiento
    def get_ano_lanzamiento(self):
        return self.__ano_lanzamiento

    def set_ano_lanzamiento(self, ano_lanzamiento):
        self.__ano_lanzamiento = ano_lanzamiento

    # Numero canciones
    def get_num_canciones(self):
        return self.__num_canciones

    def set_num_canciones(self, num_canciones):
        self.__num_canciones = num_canciones

    def antiguedad(self):
        return datetime.today().year - self.__ano_lanzamiento

    def ver_datos(self):
        print(self.__titulo, end = "")
        print(" ", end = "")
        self.__artista.show_info()
        print(" ", end = "")
        print(self.__ano_lanzamiento, self.__num_canciones)
