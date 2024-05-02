salarios = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]
abonos = []

for salario in salarios:
    abono_calculado = salario * 0.1
    
    if abono_calculado > 200:
        abonos.append(abono_calculado)
    else:
        abonos.append(200)

#Dicionário contendo os salários e os abonos:
salarios_e_abonos = {}

for i in range(0, 11):
    salarios_e_abonos[salarios[i]] = abonos[i]


#Total gasto com abonos:

total_gasto_com_abono = sum(abonos)

#Maior abono recebido:

max_abono_chave = max(salarios_e_abonos, key=salarios_e_abonos.get)
max_abono = salarios_e_abonos[max_abono_chave]

#Número de colaboradores que receberam o abono mínimo:
colaboradores_com_abono_minimo = 0

for abono in abonos:
    if abono == 200:
        colaboradores_com_abono_minimo += 1


print(f"O total gasto com abonos é de R${total_gasto_com_abono:.2f} e {colaboradores_com_abono_minimo} colaboradores receberão abono mínimo.")



    
