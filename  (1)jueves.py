class Animal:
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Peso:", self.peso, "kg")

    def comer(self):
        print(self.nombre, "está comiendo")


class Perro(Animal):
    def __init__(self, nombre, edad, peso, raza):
        super().__init__(nombre, edad, peso)
        self.raza = raza

    def ladrar(self):
        print(self.nombre, "está ladrando: ¡Guau guau!")


class Gato(Animal):
    def __init__(self, nombre, edad, peso, color):
        super().__init__(nombre, edad, peso)
        self.color = color

    def maullar(self):
        print(self.nombre, "está maullando: ¡Miau!")


class Ave(Animal):
    def __init__(self, nombre, edad, peso, tipo_de_ala):
        super().__init__(nombre, edad, peso)
        self.tipo_de_ala = tipo_de_ala

    def volar(self):
        print(self.nombre, "está volando")


class Conejo(Animal):
    def __init__(self, nombre, edad, peso, color):
        super().__init__(nombre, edad, peso)
        self.color = color

    def saltar(self):
        print(self.nombre, "está saltando")


perro1 = Perro("Luna", 3, 15, "Labrador")
perro2 = Perro("Max", 5, 20, "Beagle")

gato1 = Gato("Mishi", 2, 4, "Gris")
gato2 = Gato("Nube", 1, 3, "Blanco")

ave1 = Ave("Paco", 2, 1, "Alas grandes")
ave2 = Ave("Kiwi", 3, 1, "Alas pequeñas")

conejo1 = Conejo("Copo", 2, 2, "Blanco")
conejo2 = Conejo("Nieve", 1, 2, "Gris")


print("PERROS")
perro1.mostrar_datos()
perro1.comer()
perro1.ladrar()

perro2.mostrar_datos()
perro2.ladrar()

print("\nGATOS")
gato1.mostrar_datos()
gato1.comer()
gato1.maullar()

gato2.mostrar_datos()
gato2.maullar()

print("\nAVES")
ave1.mostrar_datos()
ave1.comer()
ave1.volar()

ave2.mostrar_datos()
ave2.volar()

print("\nCONEJOS")
conejo1.mostrar_datos()
conejo1.comer()
conejo1.saltar()

conejo2.mostrar_datos()
conejo2.saltar()