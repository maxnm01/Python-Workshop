from log_reader import read_logs
from log_analyzer import analyze_logs

def main():
    """
    Punto de entrada principal para el análisis de logs de eventos de red.
    Lee los logs, analiza el tiempo de inactividad y muestra los resultados.
    """
    # Leer los logs del archivo
    log_entries = read_logs('logs.csv')
    
    # Analizar los logs para calcular el tiempo de inactividad
    downtime = analyze_logs(log_entries)
    
    # Imprimir resultados
    for device, total_downtime in downtime.items():
        print(f"Dispositivo: {device}, Tiempo de inactividad total: {total_downtime / 60:.2f} minutos")

if __name__ == "__main__":
    main()
