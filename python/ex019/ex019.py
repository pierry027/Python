#Um professor quer sortear um dos seus quatro alunos para apagar o quadro, Faça um programa que ajude ele,lendo o nome deles e escrevendo o nome do escolhido.
import random

nome1 = str(input("Digite o nome do aluno: "))
nome2 = str(input("Digite o nome do aluno: "))
nome3 = str(input("Digite o nome do aluno: "))
nome4 = str(input("Digite o nome do aluno: "))
nomes = [nome1, nome2, nome3, nome4]
nome_ale = random.choice (nomes)
print(f"O aluno escolido foi: {nome_ale}")