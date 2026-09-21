#Desafio 013
#Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento

sal = float(input("Informe o valor do seu salario:  "))
aumen = sal * 0.15
soma = sal + aumen

print(f"Antesseu salario era de: {sal}R$ \n Agora seu salario com aumento e de {soma}R$")