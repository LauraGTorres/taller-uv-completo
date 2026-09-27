def main():
    base_str = input("Ingresa la base del rectangulo: ")
    altura_str = input("Ingrese la altura del rectángulo: ")

    base = float(base_str)
    altura = float(altura_str)

    area = base * altura

    print(f"con base de{base} y una altura de {altura}, el area calculada es: {area}")

if __name__ == "__main__":
    main()   
