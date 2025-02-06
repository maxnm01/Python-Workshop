# Introducción a Python: Sintaxis Básica, Comentarios y Buenas Prácticas

## 1. Sintaxis Básica de Python
Python es un lenguaje de programación interpretado, de alto nivel y con una sintaxis sencilla y legible. Se diseñó para ser fácil de aprender y utilizar, incluso para personas sin experiencia en programación. Veamos algunos aspectos fundamentales:

### 1.1 Declaración de Variables
En Python, no es necesario declarar el tipo de una variable, ya que es un lenguaje de tipado dinámico. Esto significa que puedes asignar valores a una variable sin especificar su tipo.

```python
nombre = "Juan"  # Variable tipo string (texto)
edad = 25  # Variable tipo entero (número sin decimales)
altura = 1.75  # Variable tipo flotante (número con decimales)
es_estudiante = True  # Variable tipo booleano (Verdadero o Falso)
```

### 1.2 Reglas para nombrar variables
- Los nombres de variables deben comenzar con una letra o un guion bajo (_).
- No pueden contener espacios ni caracteres especiales como @, #, $, %.
- Son sensibles a mayúsculas y minúsculas (ejemplo: `Edad` y `edad` son diferentes variables).
- Es recomendable usar nombres descriptivos para mayor claridad.

```python
n = 25  # Malo: el nombre no describe su propósito
edad_usuario = 25  # Bueno: describe el valor que almacena
```

### 1.3 Impresión de Datos en Consola
Para mostrar mensajes o variables en la consola, se usa la función `print()`.

```python
print("Hola, mundo!")  # Imprime un mensaje en la consola
print("Nombre:", nombre, "Edad:", edad)  # Imprime varias variables separadas por comas
```

### 1.4 Entrada de Datos
Python permite capturar datos ingresados por el usuario mediante la función `input()`, que siempre devuelve un valor de tipo string.

```python
nombre = input("Ingresa tu nombre: ")  # Captura datos desde el teclado
tipo_de_dato = type(nombre)  # Muestra el tipo de dato de la variable
print("Hola, " + nombre + "! Tu nombre es de tipo:", tipo_de_dato)
```

Si necesitas que la entrada sea un número, debes convertir el tipo de dato:

```python
edad = int(input("Ingresa tu edad: "))  # Convierte la entrada en un número entero
altura = float(input("Ingresa tu altura en metros: "))  # Convierte la entrada en un número decimal
```

### 1.5 Operaciones Matemáticas
Python permite realizar operaciones matemáticas básicas y avanzadas.

```python
suma = 10 + 5  # Suma
resta = 10 - 5  # Resta
multiplicacion = 10 * 5  # Multiplicación
division = 10 / 3  # División (devuelve un flotante)
division_entera = 10 // 3  # División entera (sin decimales)
modulo = 10 % 3  # Módulo (residuo de la división)
potencia = 2 ** 3  # Potencia (2 elevado a la 3)
```

---

## 2. Comentarios en Python
Los comentarios sirven para documentar el código y facilitar su comprensión. Se ignoran al ejecutar el programa.

### 2.1 Comentarios de una línea
Se escriben con el símbolo `#` al inicio.

```python
# Esto es un comentario en una sola línea
print("Hola, mundo!")  # Este comentario explica la función print
```

### 2.2 Comentarios de varias líneas
Se utilizan triple comillas `"""` o `'''` para documentar fragmentos largos de código.

```python
"""
Este es un comentario de varias líneas.
Se puede usar para documentar funciones o bloques de código.
"""
```

---

## 3. Buenas Prácticas en Python
Para escribir código limpio y mantenible, sigue estas recomendaciones:

### 3.1 Uso de Nombres de Variables
- Usa nombres descriptivos:
  ```python
  temperatura_celsius = 25  # Correcto
  x = 25  # Incorrecto (no es descriptivo)
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
Para documentar funciones, usa **docstrings**.

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
