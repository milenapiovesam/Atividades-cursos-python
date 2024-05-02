votos_da_marca = {"Design 1": 1334, "Design 2": 982, "Design 3": 1751, "Design 4": 210, "Design 5": 1811}

vencedor = max(votos_da_marca, key=votos_da_marca.get)

votos_vencedor = votos_da_marca[vencedor] #Para acessar o valor da maior chave baseada no valor.

total_de_votos = sum(votos_da_marca.values())

porcentagem_votos_vencedor = (votos_vencedor * 100)/total_de_votos

print(f"O vencedor é o {vencedor}, com um total de {porcentagem_votos_vencedor:.2f}% dos votos.")


