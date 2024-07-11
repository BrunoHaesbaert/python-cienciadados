import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

# Caminho para a pasta com os arquivos de texto
pasta = 'wordnet'

# Lista para armazenar todos os tokens
todos_tokens = []

# Extensões de arquivo para processar
extensoes = ['.exc', '.bib', '.rev', '.adj', '.adv', '.txt', '.noun', '.verb', '.sense']

try:
    # Processamento de cada arquivo na pasta
    for arquivo in os.listdir(pasta):
        if any(arquivo.endswith(ext) for ext in extensoes):  # Verifica as extensões
            caminho_arquivo = os.path.join(pasta, arquivo)
            with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                texto = f.read()
                # Tokenização e filtragem
                tokens = word_tokenize(texto.lower())
                filtered_tokens = [word for word in tokens if word.isalpha()]
                todos_tokens.extend(filtered_tokens)

    # Remover stopwords em inglês
    stop_words = set(stopwords.words('english'))
    todos_tokens = [word for word in todos_tokens if word not in stop_words]

    # Identificar as 50 palavras mais frequentes
    word_freqs = Counter(todos_tokens)
    top_50_words = [word for word, freq in word_freqs.most_common(50)]

    print('Top 50 palavras mais frequentes:', top_50_words)

except Exception as e:
    print('Ocorreu um erro:', e)

# Depuração: Verifique se a lista de tokens não está vazia
if not todos_tokens:
    print('Nenhum token foi coletado dos arquivos.')
