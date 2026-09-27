def main():
        nombre = input("Ingresa tu nombre: ")
        edad_str = input("Ingresa tu edad actual: ")

        edad_actual = int(edad_str)
        edad_futura = edad_actual + 5

        print(f"Hola {nombre}, tu edad actual es {edad_actual} años y dentro de cinco años tendrás {edad_futura} años.")

        if __name__ == "__main__":
            main()")
