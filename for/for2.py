#Leer un numero ingresado por el usuario
#mostrar la letra a por cada numero del 1 al numero
#ingresado por el usuario ejermplo, Numero: 3
#a
#aa
#aaa

def mostrar_Letra(numero):
    for i in range(1, numero+1):
        print(f"a"*i)

def main():
    num = int(input("Ingrese un numero: "))
    mostrar_Letra(num)

main ()