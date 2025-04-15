# Importar biblioteca de datetime
from datetime import datetime

def read_logs(file_path):
    log_entries = []

    # Abrir el archivo y leer todas las líneas
    with open(file_path, 'r') as file:
        logs = file.readlines()

    # Procesar cada línea del archivo de logs
    for log in logs:
        # Separar los elementos de la línea
        timestamp_str, level, device, event = log.strip().split(', ')

        # Convertir el string de timestamp a un objeto datetime
        timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')

        # Añadir la entrada de log a la lista
        log_entries.append((timestamp, level, device, event))

    return log_entries

#print(read_logs('logs.txt'))