import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet as wn, movie_reviews
from nltk.stem import WordNetLemmatizer
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report

# Baixar os recursos necessários
nltk.download('movie_reviews')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('stopwords')

# Função para obter a forma básica das palavras usando WordNet
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess(text):
    tokens = word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token.isalpha() and token not in stop_words]
    return ' '.join(tokens)

# Usar o corpus movie_reviews para classificação de texto
# Carregar dados
documents = [(preprocess(movie_reviews.raw(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

# Identificar as 50 palavras mais frequentes no corpus movie_reviews
all_tokens = [word for text, _ in documents for word in text.split()]
word_freqs = Counter(all_tokens)
top_50_words = [word for word, freq in word_freqs.most_common(50)]

print('Top 50 palavras mais frequentes:', top_50_words)

# Dividir dados em treino e teste
texts, labels = zip(*documents)
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

# Criar um pipeline de TF-IDF e Naive Bayes
pipeline = make_pipeline(TfidfVectorizer(), MultinomialNB())

# Treinar o modelo
pipeline.fit(X_train, y_train)

# Avaliar o modelo
y_pred = pipeline.predict(X_test)
accuracy = pipeline.score(X_test, y_test)
print(f'Acurácia: {accuracy:.2f}')

# Relatório de classificação
print(classification_report(y_test, y_pred))

