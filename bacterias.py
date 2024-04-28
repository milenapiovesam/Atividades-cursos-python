# Para um estudo envolvendo o nível de multiplicação de 
# bactérias em uma colônia, foi coletado o número de bactérias
# por dia (em milhares) e pode ser observado a seguir: 
# [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9].
# Tendo esses valores, faça um código que gere uma lista 
# contendo o percentual de crescimento de bactérias por dia,
# comparando o número de bactérias em cada dia com o número de
# bactérias do dia anterior. Dica: para calcular o percentual 
# de crescimento usamos a seguinte equação: 
# 100 * (amostra_atual - amostra_passada) / (amostra_passada).

colonia_bacterias = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]
taxa_crescimento_dia = []

#Para calcular a taxa de crescimento de cada bactéria, iteramos sobre cada dado diário e aplicamos a fórmula a ele:

for i in range(1, len(colonia_bacterias)):
    taxa_dia = 100 * (colonia_bacterias[i]- colonia_bacterias[i-1])/ (colonia_bacterias[i-1])
    taxa_dia_formatada = "{:.2f}".format(taxa_dia)
    taxa_crescimento_dia.append(taxa_dia_formatada)

print(taxa_crescimento_dia)

# Você pode usar for i in colonia_bacterias para iterar diretamente sobre os elementos 
# da lista colonia_bacterias, mas isso não fornecerá o índice i necessário para calcular a taxa 
# de crescimento entre os elementos consecutivos da lista.
# Quando você usa for i in range(1, len(colonia_bacterias)), você itera sobre os índices da lista,
#  o que permite acessar tanto o elemento atual colonia_bacterias[i] quanto o elemento 
#  anterior colonia_bacterias[i-1]. Isso é essencial para calcular a taxa de
#  crescimento entre os elementos consecutivos. Nesse caso, começo pelo índice 1 e não com o índice 0 em "range(1, len(colonia_bacterias))" 
#  porque quero a taxa de variação entre um dia e outro, o que ó pode ser obtido a partir do segundo dia (índice 1)

