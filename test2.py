# Definición de la clase base Animal
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        pass

# Definición de la clase Perro que hereda de Animal
class Perro(Animal):
    def hablar(self):
        return "Guau"

# Definición de la clase Gato que hereda de Animal
class Gato(Animal):
    def hablar(self):
        return "Miau"

# Crear instancias de Perro y Gato
animales = [Perro("Firulais"), Gato("Whiskers")]

# Iterar sobre la lista de animales y llamar al método hablar
for animal in animales:
    print(animal.nombre, animal.hablar())
