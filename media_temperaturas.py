temperaturas = []

temperatura = 0
contadora = 0

while temperatura != -273:
    temperatura = float(input("Insira uma temperatura em Celsius ou digite -273 para encerrar o programa."))

    temperaturas.append(temperatura)
    contadora += 1
    soma_temperaturas = sum(temperaturas)

    media = soma_temperaturas/contadora

print(f"A média das temperaturas é {media:.2f}.")