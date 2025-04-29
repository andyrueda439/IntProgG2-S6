def main():
    suma = 0
    while True:
        numero = int(input("Ingrese un número: "))
        suma += numero
        if suma > 100:
            break
    print("Suma total:", suma)

if __name__ == "__main__":
    main()