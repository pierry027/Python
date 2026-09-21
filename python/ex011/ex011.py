#desafio 011
#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta,pinta ua=ma área de 2m².

lar = float(input("Informe a largura: "))
alt = float(input("Informe a altura:  "))

area = lar * alt
tinta = area / 2

print(f"Precisará de {tinta} litros de tinta")