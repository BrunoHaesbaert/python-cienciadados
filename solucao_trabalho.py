import pandas as pd

file_path = 'credit_score.csv'  # caminho do seu arquivo

# Tente ler o arquivo CSV 
try:
    df = pd.read_csv(file_path, sep=';', encoding='latin-1')
except UnicodeDecodeError:
    # Tive problemas para ler o formato do arquivo
    df = pd.read_csv(file_path, sep=';', encoding='utf-16')

# Renomear colunas 
df.columns = ['case', 'name', 'date_birth', 'salary', 'gender', 'marital_status', 'country',
              'num_children', 'education_degree', 'has_car', 'own_home', 'rent_value', 'credit_score']

# Convertendo tipos de dados
df['date_birth'] = pd.to_datetime(df['date_birth'], format='%d/%m/%Y', errors='coerce')  # Convertendo para formato de data
df['gender'] = df['gender'].str.lower()  # Normalizando o gênero para minúsculas

# Calculando o total_score com os ajustes para calculo de score
df['total_score'] = (df['salary'] / 1000) - (df['num_children'] * 100) - (df['rent_value'] / 100)
df['total_score'] += (df['has_car'] * -50) + (df['own_home'] * -50)

# Exibindo os resultados calculados e os registros transformados
print('Registros do DataFrame após as transformações:')
print(df)

# Exibindo estatísticas simples do total_score
print('\nEstatísticas do total_score:')
print(df['total_score'].describe())

# Salvando o DataFrame em um arquivo CSV
output_file = 'output_dataframe.csv'
df.to_csv(output_file, index=False)

print(f'\nDataFrame salvo em {output_file} com sucesso!')