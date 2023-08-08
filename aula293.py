import csv
from pathlib import Path

PATH_CSV = Path(__file__).parent / 'aula293.csv'

with open(PATH_CSV, 'r') as file:
    reader = csv.reader(file)
    for line in reader:
        print(line)
