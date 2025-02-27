# Configuración del Entorno de Python

En este módulo, configuraremos el entorno de desarrollo que utilizaremos durante todo el curso-taller. Esto incluye la instalación de Python, Visual Studio Code (VSC), y las extensiones necesarias para trabajar de manera eficiente.

---

## Requisitos Previos

Antes de comenzar, asegúrate de contar con:
- **Sistema operativo:** Windows, macOS o Linux.
- **Permisos de administrador** para instalar software.

---

## Paso 1: Instalación de Python

1. Dirígete a la página oficial de Python: [python.org](https://www.python.org/downloads/).
2. Descarga la última versión estable de Python.
3. Durante la instalación, asegúrate de marcar la opción **"Add Python to PATH"**.
4. Verifica la instalación ejecutando en la terminal:

   ```bash
   python --version

---

## Paso 2: Instalación de Visual Studio Code
1. Descarga Visual Studio Code desde [code.visualstudio.com.](https://code.visualstudio.com/)
2. Sigue el proceso de instalación y asegúrate de seleccionar la opción "Add to PATH".

---

## Paso 3: Instalación de Extensiones en VSC
Abre Visual Studio Code y desde la barra lateral selecciona la pestaña de Extensiones (icono de cuadrados).

1. Busca e instala las siguientes extensiones:
- **Python** (Desarrollado por Microsoft)

   ![image](https://github.com/user-attachments/assets/26a26d1a-a672-40b0-b211-459fac3c545f)

- **Jupyter** (Para trabajar con notebooks)

   ![image](https://github.com/user-attachments/assets/6fcf683a-e3da-4b49-9578-af9f25887b5a)
  
- **Python Docstring Generator** (Para generar documentación)

   ![image](https://github.com/user-attachments/assets/9c9cf5d6-204f-4c6b-805d-89395c51982c)
  
- **GitLens** (Para manejar versiones en Git)

   ![image](https://github.com/user-attachments/assets/0108e506-fed5-4a91-8d1d-722eece6b731)
  
- **Prettier** (Para formatear código)

  ![image](https://github.com/user-attachments/assets/4280fd47-722b-47de-853d-9df00e15a8b9)

- **Live Share** (Para colaboración en tiempo real)

   ![image](https://github.com/user-attachments/assets/79e62eac-e2bf-4b37-bb63-118254052cbe)


---

## Paso 4: Configuración del Entorno Virtual
1. Abre una terminal en Visual Studio Code.

2. Ejecuta el siguiente comando para crear un entorno virtual:

   ```bash
   python -m venv venv

3. Activa el entorno virtual:

   - Windows:
      ```bash
      .\venv\Scripts\activate

   - macOS/Linux:
      ```bash
      source venv/bin/activate

4. Instala las bibliotecas necesarias:

   ```bash
   pip install requests paramiko netmiko

---

## Paso 5: Verificación de la Instalación
Ejecuta el siguiente script de Python para verificar que todo está correctamente configurado:

   ```python
   # verify_installation.py
   
   import os
   import sys
   import requests
   import paramiko
   import netmiko
   
   print("Verificación del entorno de Python:")
   print(f"Versión de Python: {sys.version}")
   print(f"Ruta del entorno virtual: {os.getcwd()}")
   
   print("\nVerificando bibliotecas instaladas...")
   try:
       import requests
       import paramiko
       import netmiko
       print("Todas las bibliotecas están correctamente instaladas.")
   except ImportError as e:
       print(f"Error: {e}")
   
   print("\n¡Entorno configurado correctamente!")





Para ejecutar este script, usa el siguiente comando en la terminal:

```bash
python scripts/verify_installation.py
