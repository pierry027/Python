#desafio 004

#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informaçoes possíveis sobre ele.

valor = input("Digite algo: ")

print("Tipo primitivo:", type(valor))
print("É alfanumérico?", valor.isalnum())
print("É numérico?", valor.isnumeric())
print("É alfabético?", valor.isalpha())
print("Está em maiúsculas?", valor.isupper())
print("Está em minúsculas?", valor.islower())
print("Tem espaços?", valor.isspace())
print("É um título?", valor.istitle())