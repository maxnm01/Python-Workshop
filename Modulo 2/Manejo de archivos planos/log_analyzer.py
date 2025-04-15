from collections import defaultdict

def analyze_logs(log_entries):
    """
    Analiza las entradas de logs y calcula el tiempo de inactividad de cada dispositivo.

    :param log_entries: Lista de tuplas (timestamp, level, device, event).
    :return: Diccionario con el tiempo de inactividad total por dispositivo en segundos.
    """
    # Diccionarios para almacenar eventos de Link Down y Link Up
    link_down_events = defaultdict(list)
    link_up_events = defaultdict(list)
    
    # Diccionario para almacenar el tiempo de inactividad
    downtime = defaultdict(int)
    
    # Procesar cada entrada de log
    for timestamp, level, device, event in log_entries:
        if event == 'Link Down':
            link_down_events[device].append(timestamp)
        elif event == 'Link Up':
            link_up_events[device].append(timestamp)
    
    # Calcular tiempo de inactividad para cada dispositivo
    for device, down_times in link_down_events.items():
        if device in link_up_events:
            up_times = link_up_events[device]
            down_times.sort()
            up_times.sort()
            
            # Emparejar eventos de Link Down y Link Up
            for down_time in down_times:
                up_time = next((up for up in up_times if up > down_time), None)
                if up_time:
                    downtime[device] += (up_time - down_time).total_seconds()
    
    return downtime