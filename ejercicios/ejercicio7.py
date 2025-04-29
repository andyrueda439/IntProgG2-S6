def main():
    numero = int(input("Ingrese un número entero positivo: "))
    if numero == 0:
        print("Cantidad de dígitos: 1")
        return

    digitos = 0
    while numero > 0:
        numero = numero // 10
        digitos += 1

    print("Cantidad de dígitos:", digitos)

if __name__ == "__main__":
    main()