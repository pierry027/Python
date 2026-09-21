#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção 

import math

num = float(input("Digite um número: "))
num = math.trunc (num)
print(f"O número {num}")