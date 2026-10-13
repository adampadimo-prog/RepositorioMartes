
class Vehiculo:
    def __init__(self, marca, modelo, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Velocidad: {self.velocidad} km/h")

    def acelerar(self):
        self.velocidad += 10
        print(f"{self.marca} aceleró.")
        print(f"Nueva velocidad: {self.velocidad} km/h")

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, velocidad, numero_puertas):
        super().__init__(marca, modelo, velocidad)
        self.numero_puertas = numero_puertas

    def tocar_bocina(self):
        print(f"{self.marca} {self.modelo}: ¡Piii, piii!")

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Número de puertas: {self.numero_puertas}")

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, velocidad, tipo_cilindraje):
        super().__init__(marca, modelo, velocidad)
        self.tipo_cilindraje = tipo_cilindraje

    def hacer_caballito(self):
        print(f"{self.marca} {self.modelo}: ¡La motocicleta está haciendo un caballito!")

automovil1 = Automovil("Toyota", "Corolla", 80, 4)
automovil2 = Automovil("Chevrolet", "Onix", 70, 4)

motocicleta1 = Motocicleta("Yamaha", "MT-15", 90, "155 cc")
motocicleta2 = Motocicleta("Suzuki", "GSX-R150", 100, "150 cc")

print("\n        AUTOMÓVIL 1           ")
automovil1.mostrar_informacion()
automovil1.acelerar()
automovil1.tocar_bocina()

print("\n        AUTOMÓVIL 2           ")
automovil2.mostrar_informacion()
automovil2.acelerar()
automovil2.tocar_bocina()

print("\n        MOTOCICLETA 1          ")
motocicleta1.mostrar_informacion()
motocicleta1.acelerar()
motocicleta1.hacer_caballito()

print("\n        MOTOCICLETA 2           ")
motocicleta2.mostrar_informacion()
motocicleta2.acelerar()
motocicleta2.hacer_caballito()

