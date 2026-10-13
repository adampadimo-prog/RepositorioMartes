
class Producto:

    def __init__(self, nombre, precio, codigo):
        self.nombre = nombre
        self.precio = precio
        self.codigo = codigo

    def mostrar_producto(self):
        print("Nombre:", self.nombre)
        print("Precio:", self.precio)
        print("Código:", self.codigo)

    def calcular_precio(self):
        return self.precio


class ProductoElectronico(Producto):

    def __init__(self, nombre, precio, codigo, garantia):
        super().__init__(nombre, precio, codigo)
        self.garantia = garantia

    def mostrar_garantia(self):
        print("Garantía:", self.garantia, "meses")


class ProductoAlimenticio(Producto):

    def __init__(self, nombre, precio, codigo, fecha_vencimiento):
        super().__init__(nombre, precio, codigo)
        self.fecha_vencimiento = fecha_vencimiento

    def verificar_vencimiento(self):
        print("Fecha de vencimiento:", self.fecha_vencimiento)


class Ropa(Producto):

    def __init__(self, nombre, precio, codigo, talla):
        super().__init__(nombre, precio, codigo)
        self.talla = talla

    def cambiar_talla(self, nueva_talla):
        self.talla = nueva_talla
        print("Nueva talla:", self.talla)


computador = ProductoElectronico(
    "Portátil HP",
    2900000,
    "ELE001",
    12
)

celular = ProductoElectronico(
    "Samsung A54",
    1800000,
    "ELE002",
    12
)

leche = ProductoAlimenticio(
    "Leche Alpina",
    4500,
    "ALI001",
    "2026-10-15"
)

arroz = ProductoAlimenticio(
    "Arroz Diana",
    3800,
    "ALI002",
    "2026-12-20"
)

camiseta = Ropa(
    "Camiseta deportiva",
    50000,
    "ROP001",
    "M"
)


print("===== COMPUTADOR =====")
computador.mostrar_producto()

