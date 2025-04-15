#Aquí defines la clase DispositivoRed.
from utils import obtener_vendor

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