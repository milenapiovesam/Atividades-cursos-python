diversidade_biologica = {'Área Norte': [2819, 7236],
 'Área Leste': [1440, 9492],
 'Área Sul': [5969, 7496],
 'Área Oeste': [14446, 49688],
 'Área Centro': [22558, 45148]}

dados_regioes = []
dados_numeros = []
nova_lista_somado = []

#Para somar todos os números de espécies:
for values in diversidade_biologica.values():
    for numeros in values:
        dados_numeros.append(numeros)

#Para somar o número de regiões:
for keys in diversidade_biologica.keys():
   dados_regioes.append(keys)

    
# Para calcular a média de espécies:
media_de_especies = sum(dados_numeros)/len(dados_regioes)
# print(media_de_especies)

#Para somar o número de espécies de cada região:
for values in diversidade_biologica.values():
   numero_regiao = sum(values)

#Área com maior diversidade:
area_maior_diversidade = max(diversidade_biologica, key=diversidade_biologica.get)
# print(area_maior_diversidade)

print(f"A média de espécies por área é de {media_de_especies} e a área com maior diversidade é a {area_maior_diversidade}.")








