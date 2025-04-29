import datetime

def main():
    while True:
        print("\n--- MENÚ ---")
        print("1. Saludar")
        print("2. Mostrar fecha")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("¡Hola! ¿Cómo estás?")
        elif opcion == "2":
            fecha_actual = datetime.datetime.now()
            print("Fecha actual:", fecha_actual.strftime("%d/%m/%Y %H:%M:%S"))
        elif opcion == "3":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()