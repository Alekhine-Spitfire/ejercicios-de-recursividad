#EJERCICIO DE FACTORIAL DE "n"


def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Factorial de: "))
factorial_5 = print(factorial(n))
