#Faça um programa que leia o coprimento do cateto oposto e do caa=teto adjacente de um triagunlo retagula, calcule e mostre o comprimento da hipotenusa

from math import hypot

oposto = float(input("Comprimento do cateto oposto: "))
adjacente = float(input("Comprimento do cateto adjacente: "))

hipotenusa = hypot(oposto, adjacente)

print(f"A hipotenusa mede {hipotenusa:.2f}")