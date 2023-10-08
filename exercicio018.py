#Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
angulo_graus = float(input("Digite um ângulo: "))
angulo_radianos = math.radians(angulo_graus)
seno = math.asin(angulo_radianos)
cosseno = math.acos(angulo_radianos)
tangente = math.atan(angulo_radianos)
print(seno)
print(cosseno)
print(tangente)