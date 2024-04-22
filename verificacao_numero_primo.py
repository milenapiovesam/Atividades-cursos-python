
numero_teste = int(input("Digite um número inteiro: "))
primo = True

if numero_teste <= 1:
        primo = False # A verificação do 1 e dos negativos deve ser feita fora do loop, pois o loop começa a partir do número 2.
else:
  for i in range (2, numero_teste): #Entre o dois e o primeiro número inteiro anterior ao número que estamos analisando, sempre deve haver resto na divisão.
    if numero_teste == 2: #Exceção à regra que criamos, pois 2 é divisível por 2 e mesmo assim é primo.
        primo = True
    elif numero_teste % i == 0:
        primo = False
print(primo)