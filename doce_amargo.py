# pedir 10 númros do usuário

# se for ímpar, colocar na lista amargo
# se for par, colocar na lista doce

# mostar as duas listas

amargo = []
doce = []

for i in range(0,10):
        while True: 
             try:
               id_produto = int(input("Digite o ID do produto: "))
               if id_produto % 2 == 0: 
                   doce.append(id_produto)
               else:
                   amargo.append(id_produto)
               break #O bloco for já define quando o loop While vai ser quebrado.
             except Exception: #Se não for digitado 
                  print("Digite um ID válido.")
                  

print(f"Lista de produtos doces: {doce}\nLista de produtos amargos:{amargo}")

