#Leer dos numero e imprimir los numeros entre ellos
def mostrarNumeros(inicio=0, fin=0):
    if(inicio < fin):
        for i in range(inicio, fin+1):
            print(i, end=" ")
    else:
         for i in range(inicio, fin+1):
            print(i, end=" ")

def main():
    inicio = int(input("Ingrese el primer numero: "))
    fin = int(input("Ingrese el segundo numero: "))
    mostrarNumeros(inicio, fin)

main ()