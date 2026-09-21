#O mesmo professor do desafio anterior quer sotear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random

nome1 = str(input("Digite o nome do aluno: "))
nome2 = str(input("Digite o nome do aluno: "))
nome3 = str(input("Digite o nome do aluno: "))
nome4 = str(input("Digite o nome do aluno: "))

nomes = [nome1, nome2, nome3, nome4]
random.shuffle(nomes)
print("A ordem da apresentação será:")
print(nomes)


#ex do chat gpt:

frutas = ["maçã", "banana", "uva"]
for fruta in frutas:
    print(f"{fruta}")