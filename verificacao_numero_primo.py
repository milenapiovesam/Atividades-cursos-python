
# numero_teste = int(input("Digite um número inteiro: "))
# primo = True

# if numero_teste <= 1:
#         primo = False # A verificação do 1 e dos negativos deve ser feita fora do loop, pois o loop começa a partir do número 2.
# else:
#   for i in range (2, numero_teste): #Entre o dois e o primeiro número inteiro anterior ao número que estamos analisando, sempre deve haver resto na divisão.
#     if numero_teste == 2: #Exceção à regra que criamos, pois 2 é divisível por 2 e mesmo assim é primo.
#         primo = True
#     elif numero_teste % i == 0:
#         primo = False
# print(primo)


# Exercício 5 - REVISAR, ainda não está correto
 
def conferencia_primos(): 
     numeros_primos = []
     try:
           numero = int(input("Digite um número inteiro maior que zero: "))
           if numero <= 0:
                print("Você digitou um número inválido.") # como vontar para 
                return
           else:
                for i in range(2,numero + 1):
                   verificacao_primo = True
                   for p in range(2, int(i ** 0.5) + 1): #eu estava errando essa condição
                        if i % p == 0:
                         verificacao_primo = False
                         break
                   if verificacao_primo:
                        numeros_primos.append(i)
     except ValueError:
      print("Você precisa digitar um número válido.")
    
     print(numeros_primos)
     
conferencia_primos()
input ("aperte um tecla para recomeçar: ")
conferencia_primos()

# def conferencia_primos(): 
#     numeros_primos = []
#     try:
#         numero = int(input("Digite um número inteiro maior que zero: "))
#         if numero <= 0:
#             print("Você digitou um número inválido.")
#             return
#         else:
#             for i in range(2, numero + 1):
#                 primo = True
#                 for p in range(2, int(i ** 0.5) + 1):
#                     if i % p == 0:
#                         primo = False
#                         break
#                 if primo:
#                     numeros_primos.append(i)
#     except ValueError:
#         print("Você precisa digitar um número válido.")

#     print(numeros_primos)

# conferencia_primos()
# input("Pressione qualquer tecla para recomeçar: ")
# conferencia_primos()


