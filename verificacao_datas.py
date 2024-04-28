# Verificar se um ano é bissexto:

# 2 casos:
# - O ano é divisível por 4, mas não por 100;
# - O ano é divisível por 4, por 100 e por 400.

#Verificação dos meses do ano:

# Numeração limitade entre 1 e 12;
# Meses 1, 3, 5, 7, 8, 10 e 12: até 31 dias;
# Meses 4, 6, 9 e 11: até 30 dias;
# Mês 2:
#   Se for ano bissexto: até 29 dias;
#   Se não for ano bissexto: até 28 dias.

# Nota-se que a verificação da validade ocorre dependendo do mês e do ano.

print("Bem-vendo ao programa de conferência de datas. Digite a data nos campos informados abaixo: ")
dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

conferencia_dia = False
conferencia_mes = False

if 1 <= mes <= 12:
    conferencia_mes = True

dia_maximo_fevereiro = 1

if mes == 2:
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0): #Estipula o dia máximo para o ano bissexto e o ano não bissexto.
        dia_maximo_fevereiro = 29
    else:
        dia_maximo_fevereiro = 28 

    if 1 <= dia <= dia_maximo_fevereiro:
      conferencia_dia = True
    else: 
      conferencia_dia = False

if mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if 1 <= dia <= 30:
        conferencia_dia = True
    elif 1 <= dia <= 31:
        conferencia_dia = True
    else:
         conferencia_dia = False

if conferencia_mes == True and conferencia_dia == True:
    print("Data válida.")
else:
    print("Data inválida.")




