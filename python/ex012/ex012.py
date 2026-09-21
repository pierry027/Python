#Desafio012
#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input("Informe o preço do produto: "))
desc = preco * 5 / 100
soma = preco - desc
print(f"O seu produto custava {preco}R$\n com o desconto o produto custa: {soma}R$")
