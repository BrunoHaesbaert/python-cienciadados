import csv
from statistics import mean, median, mode

class Glicemia:
    @staticmethod
    def convert_to_int(dado): # Para evitar a repetição de código para cada atributo
        return int(dado) if dado.strip() and dado.strip().isdigit() else None

    def __init__(self, dados):
        self.glicemia = self.convert_to_int(dados[3])
        self.kcal = self.convert_to_int(dados[5])
        self.carb = self.convert_to_int(dados[6])

lista_glicemia = []

# Abre o arquivo X em modo leitura
with open('glicose_data_suja.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)  # Ignora o cabeçalho
    for row in reader:
        glicemia = Glicemia(row)
        if all([glicemia.glicemia, glicemia.kcal, glicemia.carb]):  # Verifica se todos os valores são diferentes de None
            lista_glicemia.append(glicemia)

# Calcula a média
media_glicemia = mean([obj.glicemia for obj in lista_glicemia])
media_kcal = mean([obj.kcal for obj in lista_glicemia])
media_carb = mean([obj.carb for obj in lista_glicemia])

# Calcula a mediana
mediana_glicemia = median([obj.glicemia for obj in lista_glicemia])
mediana_kcal = median([obj.kcal for obj in lista_glicemia])
mediana_carb = median([obj.carb for obj in lista_glicemia])

# Calcula a moda
moda_glicemia = mode([obj.glicemia for obj in lista_glicemia])
moda_kcal = mode([obj.kcal for obj in lista_glicemia])
moda_carb = mode([obj.carb for obj in lista_glicemia])

# Mostra resultados na tela
print(f"Média de glicemia: {media_glicemia}, Kcal: {media_kcal}, Carb: {media_carb}")
print(f"Mediana de glicemia: {mediana_glicemia}, Kcal: {mediana_kcal}, Carb: {mediana_carb}")
print(f"Moda de glicemia: {moda_glicemia}, Kcal: {moda_kcal}, Carb: {moda_carb}")
