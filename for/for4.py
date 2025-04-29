#Tabla de multiplicar del número que el usuario elija (entre 1 y 12)
def mostrar_tabla(numero):
    print(f"\nTabla de multiplicar del {numero}:\n")
    for i in range(1, 13):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
def main():
    try:
        numero = int(input("Ingresa un número del 1 al 12: "))
        if 1 <= numero <= 12:
            mostrar_tabla(numero)
        else:
            print("Por favor, ingresa un número dentro del rango de 1 a 12.")
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número entero.")
    if __name__ == "_main_":
        main()