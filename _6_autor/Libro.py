class Libro:

    def __init__(self, autor, isbn, titulo):
        self.__autor = autor
        self.__isbn = isbn
        self.__titulo = titulo
        self.__num_paginas = 0

    # Titulo
    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    # Autor
    def get_autor(self):
        return self.__autor

    def set_autor(self, autor):
        self.__autor = autor

    # Isbn
    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, isbn):
        self.__isbn = isbn

    # Numero paginas
    def get_num_paginas(self):
        return self.__num_paginas

    def set_num_paginas(self, num_paginas):
        if num_paginas < 0:
            print("error")
        else:
            self.__num_paginas = num_paginas

    def ver_datos(self):
        self.__autor.ver_datos()
        print(" ", end = "")
        print(self.__isbn, self.__titulo, self.__num_paginas)
