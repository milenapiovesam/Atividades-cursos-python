

candidato_1 = []
candidato_2 = []
candidato_3 = []
candidato_4 = []
votos_nulos = []
votos_em_branco = [] 

def total_de_votos (candidato):
   soma_votos = len(candidato)
   return soma_votos

def porcentagem_votos_nulos():
   total_nulos = len(votos_nulos)
   porcentagem_nulos = total_nulos*100/20
   return porcentagem_nulos

def porcentagem_votos_em_branco():
   total_brancos = len(votos_em_branco)
   porcentagem_brancos = total_brancos*100/20
   return porcentagem_brancos

def votacao(): 
 
#  candidato_1 = []
#  candidato_2 = []
#  candidato_3 = []
#  candidato_4 = []
#  votos_nulos = []
#  votos_em_branco = []  

 for i in range(0, 21, 1):
  voto = int(input("Digite seu voto: "))

  try:
    if voto == 1:
     candidato_1.append(voto)
    elif voto == 2:
     candidato_2.append(voto)
    elif voto == 3:
     candidato_3.append(voto)
    elif voto == 4:
     candidato_4.append(voto)
    elif voto == 5:
     votos_nulos.append(voto)
    elif voto == 6:
     votos_em_branco.append(voto)
    else:
     print("Digite um valor válido para o seu voto.")
     votacao ()
  except ValueError:
    input("Digite um valor válido para o seu voto: ")
    


  soma_votos_1 = total_de_votos (candidato_1)
  soma_votos_2 = total_de_votos (candidato_2)
  soma_votos_3 = total_de_votos (candidato_3)
  soma_votos_4 = total_de_votos (candidato_4)

  porcentagem_nulos = porcentagem_votos_nulos()
  porcentagem_brancos = porcentagem_votos_em_branco()

 print(f"Votos no candidato 1:{soma_votos_1}")
 print(f"Votos no candidato 2:{soma_votos_2}")
 print(f"Votos no candidato 3:{soma_votos_3}")
 print(f"Votos no candidato 4:{soma_votos_4}")
 print(f"A porcentagem de votos em branco é: {porcentagem_brancos}%")
 print(f"A porcentagem de votos nulos é: {porcentagem_nulos}%")

votacao()