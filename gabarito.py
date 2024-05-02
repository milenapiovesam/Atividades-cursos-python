gabarito = ["d", "a", "c", "b", "a", "d", "c", "c", "a", "b"]

respostas = []
respostas_notas = []

for resposta in range(0,10): #usamos de 0 a 10 para o index coincidir com o do gabarito e na hora de apresentar ao usuário para ele identificar o número da questão, acrescentamos 1.
    resposta = input(f"Resposta da questão {resposta + 1}: ") #garante que o evento aconteça pelo menos uma vez

    while resposta not in ["a", "b", "c", "d", "e"]:

        print ("Digite uma resposta válida.")
        resposta = input(f"Resposta da questão {resposta + 1}: ")
    
    respostas.append(resposta) #ao fim de cada iteração, a lista respostas "pega a resposta fornecida"

#Depois que todas as respostas são coletadas e armazenadas na lista respostas, um novo loop é iniciado para verificar cada uma das respostas.
for i in range(0, 10):
    if respostas[i] == gabarito[i]: 
        respostas_notas.append(1)
            
soma_notas = sum(respostas_notas)
print(f"Nota:{soma_notas}")








