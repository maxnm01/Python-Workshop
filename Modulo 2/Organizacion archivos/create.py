import os
import shutil
from pathlib import Path

# 1. Crear directorio de prueba y archivos de muestra
def crear_archivos_ejemplo():
    directorio_prueba = Path("Directorio_prueba")
    directorio_prueba.mkdir(exist_ok=True)
    
    # Crear diferentes tipos de archivos
    extensiones = ["txt", "jpg", "pdf", "mp3", "xlsx", "sin_extension"]
    for ext in extensiones:
        nombre_archivo = f"archivo_prueba.{ext}" if ext != "sin_extension" else "archivo_sin_extension"
        (directorio_prueba / nombre_archivo).touch()
    
    print("¡Archivos de prueba creados con éxito!")

# 2. Script principal de organización
def organizar_archivos(ruta):
    # Diccionario de extensiones y sus carpetas
    categorias = {
        "txt": "Documentos",
        "pdf": "Documentos",
        "xlsx": "Hojas_de_Calculo",
        "jpg": "Imagenes",
        "mp3": "Musica"
    }

    ruta = Path(ruta)
    
    for archivo in ruta.iterdir():
        if archivo.is_file():
            nombre, ext = os.path.splitext(archivo.name)
            ext = ext[1:].lower()  # Quitar el punto y convertir a minúsculas
            
            # Determinar categoría
            carpeta_destino = categorias.get(ext, "Otros")
            
            # Crear ruta completa de destino
            destino = ruta / carpeta_destino
            destino.mkdir(exist_ok=True)
            
            # Mover el archivo
            try:
                shutil.move(str(archivo), str(destino / archivo.name))
                print(f"Movido: {archivo.name} -> {carpeta_destino}/")
            except Exception as e:
                print(f"Error moviendo {archivo.name}: {str(e)}")

# 3. Ejecutar el proceso completo
if __name__ == "__main__":
    # Crear archivos de prueba (ejecutar solo la primera vez)
    crear_archivos_ejemplo()
    
    # Organizar los archivos
    ruta_trabajo = Path("C:/Users/bsyst/Python-Workshop/Modulo 2/Organizacion archivos")
    organizar_archivos(ruta_trabajo)
    
    print("\n¡Organización completada!")
    print("Estructura final de directorios:")
    print("\n".join([f" - {item}" for item in sorted(ruta_trabajo.glob('*'))]))