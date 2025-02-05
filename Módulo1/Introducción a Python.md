# Introducción a Python: Sintaxis Básica, Comentarios y Buenas Prácticas

## 1. Sintaxis Básica de Python
Python es un lenguaje de programación interpretado, de alto nivel y con una sintaxis sencilla y legible. Veamos algunos aspectos fundamentales:

### Declaración de Variables
En Python, no es necesario declarar el tipo de una variable, ya que es un lenguaje de tipado dinámico.
```python
nombre = "Juan"  # Variable tipo string
edad = 25  # Variable tipo entero
altura = 1.75  # Variable tipo flotante
es_estudiante = True  # Variable tipo booleano
```

### Impresión de Datos
```python
print("Hola, mundo!")  # Imprime un mensaje en la consola
print("Nombre:", nombre, "Edad:", edad)  # Imprime varias variables en una línea
```

### Entrada de Datos
```python
nombre = input("Ingresa tu nombre: ")  # Captura datos desde el teclado
print("Hola, " + nombre + "!")  # Concatenación de strings
```

### Operaciones Matemáticas
```python
suma = 10 + 5
resta = 10 - 5
multiplicacion = 10 * 5
division = 10 / 3  # Devuelve un flotante
division_entera = 10 // 3  # Devuelve un entero
modulo = 10 % 3  # Devuelve el residuo de la división
potencia = 2 ** 3  # 2 elevado a la 3
```

## 2. Comentarios en Python
Los comentarios sirven para documentar el código y facilitar su comprensión. Existen dos tipos principales:

### Comentarios de una línea
```python
# Esto es un comentario en una sola línea
print("Hola, mundo!")  # Este comentario está al final de la línea
```

### Comentarios de varias líneas
```python
"""
Este es un comentario de varias líneas.
Se puede usar para documentar funciones o bloques de código.
"""
```

## 3. Buenas Prácticas en Python
### 3.1 Uso de Nombres de Variables
- Usa nombres descriptivos:
  ```python
  temperatura_celsius = 25
  velocidad_auto = 80
  ```
- Sigue la convención **snake_case**:
  ```python
  numero_de_empleados = 50  # Correcto
  NumeroDeEmpleados = 50  # Incorrecto (convención camelCase no es habitual en Python)
  ```

### 3.2 Mantener un Código Legible
- Usa indentación de **4 espacios** por nivel de anidación:
  ```python
  if edad >= 18:
      print("Eres mayor de edad.")
  ```
- Evita líneas de código demasiado largas (>79 caracteres).

### 3.3 Uso de Comentarios
- Comenta solo cuando sea necesario y evita comentarios obvios:
  ```python
  # MALO
  x = x + 1  # Incrementa x en 1

  # BUENO
  contador += 1  # Aumenta el contador para registrar un nuevo usuario
  ```

### 3.4 Uso de Docstrings en Funciones
```python
def sumar(a, b):
    """Devuelve la suma de dos números."""
    return a + b
```

### 3.5 Manejo de Errores con Try-Except
Evita que tu programa se detenga debido a errores inesperados:
```python
try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
    print("Resultado:", resultado)
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
except ValueError:
    print("Error: Ingresa un número válido.")
```

