# Mese para acessar o nome pelo index:
meses =["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

temperaturas = []

meses_acima_da_media = {}

for i in range(0, 12):
    temperatura_mes = float(input(f"Informe a temperatura do mês de {meses[i]}: "))
    temperaturas.append(temperatura_mes)

soma_temperaturas = sum(temperaturas)

media_anual_temp = soma_temperaturas / 12

for i in range (0, 12):
    if temperaturas[i] > media_anual_temp:
        meses_acima_da_media[meses[i]] = temperaturas [i]

for keys, values in meses_acima_da_media.items():
    print(f"Meses com temperaturas acima da média anual:\n {keys,values}")







