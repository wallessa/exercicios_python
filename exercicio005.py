#Exercício Python 005: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
num = int(input("Insira um número: "))
antecessor = num-1
sucessor = num+1
print(f"O antecessor do número {num} é {antecessor} e o sucessor é {sucessor}")