#Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import sqrt
cateto_oposto = float(input("Insira o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Insira o comprimento do cateto adjacente: "))
calculo = (cateto_oposto**2 + cateto_adjacente**2)
hipotenusa = sqrt(calculo)
print(f"A hipotenusa do triângulo é {hipotenusa}")
