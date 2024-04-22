def iniciar_programa():

 idade = int(input("Informe a idade do cliente: "))


 idade_0_25 = []
 idade_26_50 = []
 idade_51_75 = []
 idade_76_100 = []

 try:
  while idade > 0:
   if 0 <= idade <= 25:
    idade_0_25.append(idade)
    idade = int(input("Informe a idade do cliente: "))
   elif 26 <= idade <= 50:
    idade_26_50.append(idade)
    idade = int(input("Informe a idade do cliente: "))
   elif 51 <= idade <= 75:
    idade_51_75.append(idade)
    idade = int(input("Informe a idade do cliente: "))
   elif 76 <= idade <= 100:
    idade_76_100.append(idade)
    idade = int(input("Informe a idade do cliente: "))
   else:
    break
 except ValueError: 
  print("Você precisa digitar um valor válido.")
  iniciar_programa()
  
 print("Clientes de 0 a 25 anos:", idade_0_25)
 print("Clientes de 26 a 50 anos:", idade_26_50)
 print("Clientes de 51 a 75 anos:", idade_51_75)
 print("Clientes de 76 a 100 anos:", idade_76_100)

iniciar_programa()