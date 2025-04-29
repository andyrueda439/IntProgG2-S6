def main():
    suma = 0
    contador = 0

    while True:
        calificacion = float(input("Ingrese una calificación (-1 para terminar): "))
        if calificacion == -1:
            break
        suma += calificacion
        contador += 1

    if contador > 0:
        promedio = suma / contador
        print("Promedio de calificaciones:", promedio)
    else:
        print("No se ingresaron calificaciones.")

if __name__ == "__main__":
    main()