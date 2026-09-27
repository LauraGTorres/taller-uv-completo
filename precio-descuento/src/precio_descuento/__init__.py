def main():
    precio_str = input("Ingresa el precio original del producto:")

    precio_original = float(precio_str)
    descuento = precio_original * 0.10
    precio_final = precio_original - descuento

    print(f"Precio original: {precio_original}")
    print(f"Descuen (10%): {descuento}")
    print(f"Precio final a pagar: {precio_final}")

if __name__ == "__main__":
   main()
