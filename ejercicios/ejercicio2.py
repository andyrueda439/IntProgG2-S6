def main():
    limite = int(input("Ingrese un número positivo: "))
    contador = 0
    while contador <= limite:
        if contador % 2 == 0:
            print(contador)
        contador += 1

if __name__ == "__main__":
    main()