# log_reader.py
import pandas as pd

def read_logs(file_path):
    """
    Lee un archivo Excel de logs y devuelve un DataFrame de pandas con las entradas de logs.

    :param file_path: Ruta del archivo de logs Excel.
    :return: DataFrame de pandas con columnas: ['timestamp', 'level', 'device', 'event'].
    """
    # Leer el archivo Excel en un DataFrame de pandas
    log_df = pd.read_excel(file_path)
    
    # Convertir la columna 'timestamp' a tipo datetime
    log_df['timestamp'] = pd.to_datetime(log_df['timestamp'], format='%Y-%m-%d %H:%M:%S')
    
    return log_df


# log_analyzer.py
def analyze_logs(log_df):
    """
    Analiza el DataFrame de logs y calcula el tiempo de inactividad de cada dispositivo.

    :param log_df: DataFrame de pandas con columnas: ['timestamp', 'level', 'device', 'event'].
    :return: Diccionario con el tiempo de inactividad total por dispositivo en segundos.
    """
    # Filtrar los eventos de Link Down y Link Up
    link_down_df = log_df[log_df['event'] == 'Link Down']
    link_up_df = log_df[log_df['event'] == 'Link Up']
    
    # Diccionario para almacenar el tiempo de inactividad
    downtime = defaultdict(int)
    
    # Procesar cada dispositivo
    devices = log_df['device'].unique()
    for device in devices:
        device_downs = link_down_df[link_down_df['device'] == device].sort_values('timestamp')
        device_ups = link_up_df[link_up_df['device'] == device].sort_values('timestamp')
        
        down_times = device_downs['timestamp'].tolist()
        up_times = device_ups['timestamp'].tolist()
        
        # Emparejar eventos de Link Down y Link Up
        for down_time in down_times:
            up_time = next((up for up in up_times if up > down_time), None)
            if up_time:
                downtime[device] += (up_time - down_time).total_seconds()
    
    return downtime


# main.py
from log_reader import read_logs
from log_analyzer import analyze_logs

def main():
    """
    Punto de entrada principal para el análisis de logs de eventos de red.
    Lee los logs, analiza el tiempo de inactividad y muestra los resultados.
    """
    # Leer los logs del archivo Excel
    log_df = read_logs('logs.xlsx')
    
    # Analizar los logs para calcular el tiempo de inactividad
    downtime = analyze_logs(log_df)
    
    # Imprimir resultados
    for device, total_downtime in downtime.items():
        print(f"Dispositivo: {device}, Tiempo de inactividad total: {total_downtime / 60:.2f} minutos")

if __name__ == "__main__":
    main()
