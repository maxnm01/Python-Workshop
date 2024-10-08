## **Taller de Python - Entorno de Desarrollo y Automatización**

Este repositorio contiene las instrucciones y archivos necesarios para configurar tu entorno de desarrollo con Python y Visual Studio Code, junto con las bibliotecas y extensiones que utilizaremos durante el taller.

### **Instrucciones**

### **1. Clonar este Repositorio**

Para comenzar, clona este repositorio en tu equipo local ejecutando el siguiente comando en la terminal o consola de Git:

```bash
git clone https://github.com/tu_usuario/nombre_del_repositorio.git
cd nombre_del_repositorio
```

### **2. Instalación de Visual Studio Code**

1. Descarga Visual Studio Code desde su [sitio oficial](https://code.visualstudio.com/).
2. Sigue las instrucciones de instalación según tu sistema operativo.
3. Abre Visual Studio Code una vez instalado.

### **3. Instalación de Python**

1. Descarga e instala Python desde [python.org](https://www.python.org/downloads/).
2. Durante la instalación, selecciona la opción **"Add Python to PATH"**.
3. Verifica la instalación ejecutando el siguiente comando en la terminal:

   ```bash
   python --version
   ```

   Deberías ver una versión de Python 3.x instalada.

### **4. Configuración del Entorno Virtual**

Es recomendable crear un entorno virtual para mantener las bibliotecas organizadas y separadas de otros proyectos.

1. **Crear el entorno virtual**:
   - Ejecuta los siguientes comandos dentro del directorio del repositorio clonado:
     ```bash
     python -m venv venv
     ```
   - Esto creará un entorno virtual llamado `venv`.

2. **Activar el entorno virtual**:
   - En Windows:
     ```bash
     venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Instalar las bibliotecas necesarias**:
   - Una vez activado el entorno virtual, instala las bibliotecas requeridas ejecutando:
     ```bash
     pip install -r requirements.txt
     ```

### **5. Extensiones de Visual Studio Code**

Instala las siguientes extensiones desde el Marketplace de Visual Studio Code para mejorar la experiencia de desarrollo con Python:

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
- [Python Docstring Generator](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)
- [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)
- [GitHub Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot) (opcional)
- [Prettier - Code Formatter](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)

### **6. Configuración del Entorno en Visual Studio Code**

1. **Seleccionar el intérprete de Python:**
   - Abre Visual Studio Code y selecciona el intérprete de Python que has instalado o el entorno virtual creado. Para hacerlo, ve a la parte inferior izquierda y selecciona `Python: Select Interpreter`.

2. **Configurar GitHub Copilot (opcional):**
   - Si decides usar GitHub Copilot, abre la extensión y sigue las instrucciones para iniciar sesión con tu cuenta de GitHub.

3. **Abrir Jupyter Notebooks:**
   - Si necesitas trabajar con notebooks, abre un archivo con extensión `.ipynb` o crea uno nuevo desde `File -> New File -> Jupyter Notebook`.

### **7. Ejecución de Código y Verificación del Entorno**

Para verificar que tu entorno esté correctamente configurado:

1. Crea un archivo `hello_world.py` en el directorio del repositorio con el siguiente contenido:

   ```python
   print("¡Hola, Mundo!")
   ```

2. Ejecuta el archivo desde la terminal de VSC:

   ```bash
   python hello_world.py
   ```

3. También puedes crear un notebook (`.ipynb`) y ejecutar una celda con el siguiente código:

   ```python
   import pandas as pd
   print("Este es un notebook ejecutándose en Visual Studio Code")
   ```

---

### **8. Estructura del Repositorio**

- `README.md`: Instrucciones y guía de instalación.
- `requirements.txt`: Lista de dependencias y bibliotecas necesarias.
- `/notebooks`: Directorio con ejemplos de notebooks.
- `/scripts`: Directorio con scripts Python que serán utilizados en el taller.
- `/data`: Directorio para archivos de datos (Excel, CSV, etc.).

---

### **9. Actualización de Dependencias**

Si en algún momento es necesario instalar nuevas bibliotecas, puedes hacerlo ejecutando `pip install <nombre_biblioteca>` y luego guardar la nueva lista de dependencias en `requirements.txt` con el siguiente comando:

```bash
pip freeze > requirements.txt
```

Esto mantendrá el archivo actualizado para futuros colaboradores.

---

### **10. Apoyo y Comunicación**

Este repositorio también está habilitado para colaborar en GitHub a través de la creación de **Issues** para preguntas y aportaciones de los colaboradores. Además, puedes usar **Pull Requests** para subir tus propias contribuciones (código, notebooks, casos de uso).
