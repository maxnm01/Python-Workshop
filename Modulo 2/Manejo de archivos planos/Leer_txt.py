# Leer archivo tipo txt
'''
with open('logs.txt','r') as file:
    logs = file.readlines()
    print(logs)
'''
import csv

# Leer archivos tipo csv

with open('logs.csv', 'r') as file:
        logs = file.readlines()
        #reader = csv.reader(file)
        #next(reader)
        print(logs)
