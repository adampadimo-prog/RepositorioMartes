P = float(input("Ingrese el capital inicial: "))
r = float(input("Ingrese la tasa de interés anual (%): ")) / 100
años = int(input("¿Cuántos años desea calcular?: "))

print("\n--------------------------------")
print("       TABLA DE INTERÉS")
print("--------------------------------")
print("Año\tCapital final")
print("--------------------------------")

for año in range(1, años + 1):
    A = P * (1 + r) ** año
    print(año, "\t$", round(A, 2))

print("--------------------------------")