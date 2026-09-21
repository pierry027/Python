#Desafio 007
#desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.


n1 = float(input("Informe a sua primeira nota: "))
n2 = float(input("Informe sua segunda nota: "))
media = (n1 + n2) / 2

print("========Soma========== \n")
print(f" {n1} + {n2} / 2")
print("Calculando...")
print(f"A sua media foi de {media}")