def metros_a_centimetros(metros: float) -> float:
    return metros * 100


def metros_a_milimetros(metros: float) -> float:
    return metros * 1000


def main() -> None:
    print("--- CONVERSOR DE LONGITUD ---")
    
    metros = float(input("Ingrese la cantidad en metros: "))
    
    centimetros = metros_a_centimetros(metros)
    milimetros = metros_a_milimetros(metros)
    
    print(f"{metros} metros equivalen a {centimetros} centímetros")
    print(f"{metros} metros equivalen a {milimetros} milímetros")


if __name__ == "__main__":
    main()