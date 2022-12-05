# Autor: “Carlos, Ruiz Zafón”,”25 de septiembre de 1964”, “España”
# o Libro de Carlos Ruiz Zafón: ISBN: “9788408105824”, Título: “El
# prisionero del Cielo”, páginas: 245
# o Intenta asignar como fecha de nacimiento el 1/1/2020 al objeto Autor y
# -100 como número de páginas al objeto Libro.(Se deberían mostrar los
# errores por pantalla y no modificar el valor de los atributos)
# o Visualiza por pantalla los datos del libro (visualizará también los datos
# de su autor)
from _6_autor.Autor import Autor
from _6_autor.Libro import Libro

autor = Autor("Carlos", "Ruiz Zafón")
autor.set_ano_nacimiento(1964)
autor.set_pais("Espana")

libro = Libro(autor, "9788408105824", "El prisionero del Cielo")
libro.set_num_paginas(245)

# -100
libro.set_num_paginas(-100)

libro.ver_datos()
