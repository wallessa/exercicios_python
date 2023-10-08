#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
from math import sqrt
num = int(input("Insira um número: "))
dobro = num*2
triplo = num*3
raiz = sqrt(num)
print(f"O dobro de {num} é {dobro}\nO triplo de {num} é {triplo} \nA raiz quadrada de {num} é {raiz:.2f}")