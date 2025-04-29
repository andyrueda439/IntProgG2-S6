def main():
    contador = 1
    suma = 0

    while contador <= 100:
        if contador % 2 != 0:
            suma += contador
        contador += 1

    print("Suma de los números impares del 1 al 100:", suma)

if __name__ == "__main__":
    main()