#Desafio 016
#Escreva um programa que pergunte a quantidade de km percorridos por carro alugado e a quantidade de dias pelos quais foi alugado.Calcule o preço a pagar. sabendo que o carro custa R$60 por dia e R$0,15 pro km rodado.

perc = float(input("Informe a quantidade de km percorridos:   "))
alugado = int(input("Informe a quantidade de dias pelos quais foi alugado:  "))

pago = perc * 0.15
valordia = alugado * 60
soma = pago + valordia
print(f"\n Você terá que pagar de km rodados: {pago}R$\n é de dia usados {valordia}R$\n somando tudo deu {soma}R$")
 