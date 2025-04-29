def main():
    numero = int(input("Ingrese un número entero positivo: "))
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

if __name__ == "__main__":
    main()