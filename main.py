class Libro:
    def __init__(self, titulo, author, ISBN, disponible=True):
        self.titulo = titulo
        self.author = author
        self.ISBN = ISBN
        self.disponible = disponible
        self.__veces_prestado = 0

    def prestar(self):
        if self.disponible:
            self.disponible = False
            self.__veces_prestado += 1
            return f"{self.titulo} prestado con éxito. Total de veces prestado: {self.__veces_prestado}"
        return f"{self.titulo} no está disponible para préstamo."

    def devolver(self):
        self.disponible = True
        return f"{self.titulo} devuelto con éxito."

    def __str__(self):
        return f"{self.titulo} por {self.author} disponible: {self.disponible}"

    def es_popular(self):
        return self.__veces_prestado > 5

    def get_veces_prestado(self):
        return self.__veces_prestado

    def set_veces_prestado(self, veces_prestado):
        self.__veces_prestado = veces_prestado


mi_libro = Libro("El Quijote", "Miguel de Cervantes", "978-3-16-148410-0", True)
otro_libro = Libro(
    "Cien años de soledad", "Gabriel García Márquez", "978-0-525-95014-1", True
)

mi_libro.set_veces_prestado(10)
print(mi_libro.get_veces_prestado())
print(mi_libro.prestar())
print(mi_libro.prestar())
print(mi_libro.devolver())


catalogo = [
    mi_libro,
    otro_libro,
]  # se crea una lista con los objetos libro, se pueden agregar más libros a la lista y luego iterar sobre ella para mostrar su información.
# print(type(catalogo))
# print(catalogo)

for libro in catalogo:
    print(libro)


print(
    catalogo[0].titulo
)  # se accede al título del primer libro en la lista utilizando el índice 0 y el atributo titulo del objeto libro.

print(catalogo[1].es_popular())  # se llama al método es_popular()
