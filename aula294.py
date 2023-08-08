import csv
from pathlib import Path

PATH_CSV = Path(__file__).parent / 'aula293.csv'
lista_clientes = []
with open(PATH_CSV, 'r') as fileReader:
    reader = csv.DictReader(fileReader)
    for line in reader:
        lista_clientes.append(line)
    print(lista_clientes)
fileReader.close()

PATH_CSV_WRITE = Path(__file__).parent / 'aula294.csv'

# with open(PATH_CSV_WRITE, 'w') as fileWrite:
#     columns = lista_clientes[0].keys()
#     reader = csv.writer(fileWrite)

#     reader.writerow(columns)

#     for clientes in lista_clientes:
#         reader.writerow(clientes.values())
# fileWrite.close()

with open(PATH_CSV_WRITE, 'w') as fileWrite:
    columns = lista_clientes[0].keys()
    reader = csv.DictWriter(fileWrite, fieldnames=columns)

    reader.writeheader()

    for clientes in lista_clientes:
        reader.writerow(clientes)
fileWrite.close()
