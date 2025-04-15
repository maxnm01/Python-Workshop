import pdb

def factorial(n):
    resultado = 1
    pdb.set_trace()  # Punto de quiebre
    for i in range(n):
        resultado *= i
    return resultado

print(factorial(5))