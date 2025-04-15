#Aquí es donde se ejecuta tu aplicación principal. 
# Importas las clases y funciones de los otros módulos y las usas.
from dispositivo_red import DispositivoRed

def main():
    # Lista de dispositivos de red
    dispositivos = [
        {'nombre': 'Switch1', 'modelo': '2960'},
        {'nombre': 'Router1', 'modelo': '6509'},
        {'nombre': 'Switch2', 'modelo': 'QFX5100'},
        {'nombre': 'Router2', 'modelo': 'MX480'},
        {'nombre': 'Switch3', 'modelo': 'EX4300'}
    ]

    # Crear instancias de DispositivoRed y mostrar información
    lista_dispositivos = [DispositivoRed(d['nombre'], d['modelo']) for d in dispositivos]

    for dispositivo in lista_dispositivos:
        dispositivo.mostrar_info()
        print('---')

if __name__ == "__main__":
    main()