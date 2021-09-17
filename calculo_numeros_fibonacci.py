def fibo():
    print("Bienvenido al algoritmo que te dice los numeros fibonacci que existen, solo introduces la cantidad de numeros fibonacci que quieres y te mostrara una lista ordenada de la cantidad que pediste")
    veces_fibo = int(input("¿Cuantas numeros fibonacci quieres saber?: "))
    fibo = 0
    fibo2 = 0
    for i in range(1, veces_fibo - 1):
        fibo_lista = []
        if fibo == 0:
            fibo = 1
            fibo2 = 1
            print(f"El fibonacci numero 1 es {fibo}")
            print(f"El fibonacci numero 2 es {fibo}")
            fibo3 = fibo + fibo2
            print(f"El fibonacci numero 3 es {fibo3}")
            fibo = fibo3
        else:
            fibo3 = fibo + fibo2
            print(f"El fibonacci numero {i + 2} es {fibo3}")
            fibo2 = fibo
            fibo = fibo3


if __name__ == "__main__":
    fibo()