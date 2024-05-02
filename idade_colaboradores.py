idade_colaboradores = {'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
 'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
 'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
 'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}

# Média da idade de cada setor
lista_media_idade_setor = []

for values in idade_colaboradores.values():
    media_idade_setor = sum(values)/len(values)
    lista_media_idade_setor.append(media_idade_setor)

print(lista_media_idade_setor)

#Para montar um dicionário com as médias de cada setor:
setores = []
novo_dicionario = {}

for keys in idade_colaboradores.keys():
    setores.append(keys)

novo_dicionario = dict(zip(setores, lista_media_idade_setor))

novo_dicionario_apresentavel = novo_dicionario.items()

print(f"A média de idades por setor é: {novo_dicionario_apresentavel}")
#Média de todos os setores:

for values in idade_colaboradores.values():
    media_idade_geral = sum(values)/len(values)

print(f"A média da idade geral entre os colaboradores é de {media_idade_geral:.1f} anos.")

#Pessoas com idade acima e abaixo da média:

idade_acima_da_media = []
idade_abaixo_da_media = []

for values in idade_colaboradores.values():
    for idade in values:
        if idade > media_idade_geral:
            idade_acima_da_media.append(idade)
        if idade < media_idade_geral:
            idade_abaixo_da_media.append(idade)

pessoas_idade_acima = len(idade_acima_da_media)
pessoas_idade_abaixo = len(idade_abaixo_da_media)

print(f"{pessoas_idade_abaixo} colaboradores estão abaixo da idade média de idade, enquanto {idade_abaixo_da_media} estão acima.")









