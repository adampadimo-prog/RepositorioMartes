print("==========================================")
print("   SISTEMA DE SELECCIÓN DE PROVEEDORES")
print("==========================================")

proveedores = []

cantidad = int(input("¿Cuántos proveedores desea registrar? "))

for i in range(cantidad):

    print("\n------------------------------------------")
    print("Proveedor", i + 1)
    print("------------------------------------------")

    nombre = input("Nombre del proveedor: ")

    print("\nIngrese las calificaciones de 0 a 100")

    precio = float(input("Precio: "))
    calidad = float(input("Calidad: "))
    entrega = float(input("Entrega: "))
    servicio = float(input("Servicio: "))
    riesgo = float(input("Riesgo: "))

    # Fórmula
    calificacion = (
        (0.25 * precio) +
        (0.30 * calidad) +
        (0.20 * entrega) +
        (0.15 * servicio) +
        (0.10 * riesgo)
    )

    # Guardar proveedor
    proveedor = {
        "nombre": nombre,
        "precio": precio,
        "calidad": calidad,
        "entrega": entrega,
        "servicio": servicio,
        "riesgo": riesgo,
        "calificacion": calificacion
    }

    proveedores.append(proveedor)


# Ordenar de mayor a menor calificación
proveedores.sort(key=lambda x: x["calificacion"], reverse=True)


print("\n==========================================")
print("       RANKING DE PROVEEDORES")
print("==========================================")

for i, proveedor in enumerate(proveedores, start=1):

    print(
        i, ".",
        proveedor["nombre"],
        "- Calificación:",
        round(proveedor["calificacion"], 1)
    )


print("\n==========================================")
print("           MEJOR PROVEEDOR")
print("==========================================")

mejor = proveedores[0]

print("Proveedor:", mejor["nombre"])
print("Calificación:", round(mejor["calificacion"], 1), "/ 100")