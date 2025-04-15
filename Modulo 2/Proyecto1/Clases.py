# Función para obtener vendor
def obtener_vendor(modelo):
    vendors = {
        '2960': 'Cisco',
        '6509': 'Cisco',
        'QFX5100': 'Juniper',
        'EX4300': 'Juniper',
        'MX480': 'Juniper',
    }
    return vendors.get(modelo, 'Vendor desconocido')

# Ejemplo de uso
#modelo = '2960'
#print(f'El vendor del modelo {modelo} es {obtener_vendor(modelo)}')

# Definición de la clase Dispositivo Red
class DispositivoRed:
    def __init__(self, nombre, modelo):
        self.nombre = nombre
        self.modelo = modelo
        self.vendor = obtener_vendor(modelo)

    def mostrar_info(self):
        print(f'Nombre: {self.nombre}')
        print(f'Modelo: {self.modelo}')
        print(f'Vendor: {self.vendor}')

# Ejemplo de uso
#dispositivo = DispositivoRed('Switch1', '2960')
#dispositivo.mostrar_info()


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
