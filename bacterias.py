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
    taxa_dia = 100 * (colonia_bacterias[i] - colonia_bacterias[i-1])/ (colonia_bacterias[i-1])
    taxa_dia_formatada = "{:.2f}".format(taxa_dia)
    taxa_crescimento_dia.append(taxa_dia_formatada)

print(taxa_crescimento_dia)

