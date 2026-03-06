class Libro:
    def __init__(self, titulo, author, ISBN, disponible=True):
        self.titulo = titulo
        self.author = author
        self.ISBN = ISBN
        self.disponible = disponible

    def prestar(self):
        if self.disponible:
            self.disponible = False
        return f"{self.titulo} prestado con éxito."

    def devolver(self):
        self.disponible = True
        return f"{self.titulo} devuelto con éxito."

    def __str__(self):
        return f"{self.titulo} por {self.author} disponible: {self.disponible}"


mi_libro = Libro("El Quijote", "Miguel de Cervantes", "978-3-16-148410-0", False)
otro_libro = Libro(
    "Cien años de soledad", "Gabriel García Márquez", "978-0-525-95014-1", True
)

print(mi_libro.prestar())
print(mi_libro.devolver())


catalogo = [mi_libro, otro_libro]

for libro in catalogo:
    print(libro)
