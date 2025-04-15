def factorial(n):
    resultado = 1
    print(f"Valor inicial: {resultado}")  # Debug point 1
    
    for i in range(n):
        print(f"Multiplicando por i={i}")  # Debug point 2
        resultado *= i
        print(f"Resultado parcial: {resultado}")  # Debug point 3
    
    return resultado

print(factorial(5))
