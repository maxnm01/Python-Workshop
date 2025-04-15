def factorial(n):
    resultado = 1
    for i in range(n):
        resultado *= i
    return resultado

print(factorial(5))  # Debería devolver 120, pero devuelve 0