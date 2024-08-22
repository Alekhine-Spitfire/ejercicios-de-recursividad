#DEL "CURSO DE ESTRUCTURAS DE DATOS LINEALES CON PYTHON" DE PLATZI

#EJERCICIO DE SUMA EN FORMA DE PIRÁMIDE



def pyramid_sum(lower, upper, margin=0):
    
    blanks = " " * margin
    print(blanks, lower, upper)
    
    if lower > upper:
        print(blanks, 0)
        return 0
    else:
        result = lower + pyramid_sum(lower + 1, upper, margin +4)
        print(blanks, result)
        return result
    
pyramid_sum(1, 4)
