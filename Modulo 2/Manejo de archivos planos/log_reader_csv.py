import csv
from datetime import datetime

def read_logs(file_path):
    """
    Lee un archivo CSV de logs y devuelve una lista de entradas de logs.

    :param file_path: Ruta del archivo de logs CSV.
    :return: Lista de tuplas (timestamp, level, device, event).
    """
    log_entries = []

    # Abrir el archivo CSV y leer las líneas
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Saltar la cabecera del CSV

        # Procesar cada línea del archivo CSV
        for row in reader:
            timestamp_str, level, device, event = row
            # Convertir el string de timestamp a un objeto datetime
            timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
            # Añadir la entrada de log a la lista
            log_entries.append((timestamp, level, device, event))
    
    return log_entries

print(read_logs('logs.csv'))