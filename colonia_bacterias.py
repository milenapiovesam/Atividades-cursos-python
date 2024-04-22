numero_de_elementosA = 4
numero_de_elementosB = 10
dias = 0

#Não sei quantos dias vai levar, não sei quantas iterações serão necessárias para que isso ocorra. Logo, uso while.

while numero_de_elementosA != numero_de_elementosB:

  numero_de_elementosA += numero_de_elementosA * 0.15
  numero_de_elementosB += numero_de_elementosA * 0.3
  dias += 1 #Conto os dias para poder exibir o número de iterações.

print("A colônia A alcançará a colônia B em", dias,"dias.")