def main():
    n = int(input("Ingrese la cantidad de números de la serie Fibonacci: "))
    a, b = 0, 1

    for i in range(n):
        print(a)
        a, b = b, a + b

if __name__ == "__main__":
    main()