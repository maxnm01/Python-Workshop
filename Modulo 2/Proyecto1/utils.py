#Aquí defines la función obtener_vendor y otras funciones auxiliares si es necesario
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
#modelo = '6509'
#print(f'El vendor del modelo {modelo} es {obtener_vendor(modelo)}')