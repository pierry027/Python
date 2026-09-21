#Desafio 008
#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metro =float(input("Informe o valor do metro:  "))
centi = metro * 100
mili = metro * 1000

print(f"Este valor convertido em centímetros: {centi} \n Este valor em milímetros: {mili}")