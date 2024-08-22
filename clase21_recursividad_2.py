#EJERCICIO DE FIBONACCI


'''

def fibonacci(n):
    if n == 0:
        return 0
    
    elif n == 1:
        return 1
    
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
number = 3

print(fibonacci(3))

#0 1 1 2 3 5 8



#EJERCICIO DE FIBONACCI VARIANTE

'''
def fib_r(n):
    if n < 2:
        return n
    else:
        return fib_r(n-1) + fib_r(n-2)

n = int(input("Ingrese la cantidad de elementos para fibonacci: "))

for x in range(n):
    print(fib_r(x))
    
