# Leer archivos de texto
with open('logs.txt', 'r') as file:
        logs = file.readlines()
        print(logs)