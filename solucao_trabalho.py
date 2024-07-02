import csv
from datetime import datetime

def parse_date(date_str):
    try:
        return datetime.strptime(date_str, '%d/%m/%Y').date()
    except ValueError:
        return None

def parse_int(value):
    try:
        return int(value)
    except ValueError:
        return None

def parse_float(value):
    try:
        return float(value)
    except ValueError:
        return None

def process_row(row):
    row[2] = parse_date(row[2])  # Convert date of birth
    row[3] = parse_int(row[3])   # Convert salary
    row[7] = parse_int(row[7])   # Convert number of sons
    row[10] = parse_float(row[10])  # Convert rent value
    return row

# Abra o arquivo CSV
with open('credit_score.csv', 'r') as arquivo_csv:
    leitor = csv.reader(arquivo_csv, delimiter=';')

    # Pule o cabeçalho
    next(leitor)

    # Itere sobre as linhas do arquivo
    for linha in leitor:
        linha_processada = process_row(linha)
        print(linha_processada)
