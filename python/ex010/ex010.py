#Desafio 010
#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar 
#considere USS1,00 = R$3,27

dinhe = float(input("Informe seu dinheiro:  "))
soma = dinhe / 3.27

print(f"Você pode comprar {soma:.2f} Dólares")