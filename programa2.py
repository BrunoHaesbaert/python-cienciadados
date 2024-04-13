from statistics import median, mode

def classificar_valores(lista):
    valores_classificados = []
    for numero in lista:
        if numero < 80:
            valores_classificados.append('abaixo')
        elif 80 <= numero <= 140:
            valores_classificados.append('normal')
        else:
            valores_classificados.append('acima')
    return valores_classificados

# Valores fixos
numeros = [100, 98, 78, 45, 238, 390, 67, 98, 100, 98, 100, 98, 67, 55]

# Classificar os valores
valores_classificados = classificar_valores(numeros)

# Calcular média, mediana e moda
media = sum(numeros) / len(numeros)
mediana = median(numeros)
moda = mode(numeros)

# Contar a quantidade de vezes que o número foi menor que 70
hipoglicemia = sum(1 for numero in numeros if numero < 70)

# Calcular a porcentagem de hipoglicemia
porcentagem_hipoglicemia = (hipoglicemia / len(numeros)) * 100
porcentagem_hipoglicemia = round(porcentagem_hipoglicemia, 2)

# Armazenar os resultados em uma lista
resultados = []
resultados.append(["Lista original:", numeros])
resultados.append(["Lista com valores classificados:", valores_classificados])
resultados.append(["Média dos valores:", media])
resultados.append(["Mediana dos valores:", mediana])
resultados.append(["Moda dos valores:", moda])
resultados.append(["Hipoglicemia:", hipoglicemia])
resultados.append(["Porcentagem de hipoglicemia:", porcentagem_hipoglicemia])

# Imprimir os resultados
for resultado in resultados:
    print(*resultado)