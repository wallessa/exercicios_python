#Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = input("Insira seu nome completo: ")
print("Seu primeiro nome é: ")
lista_nomes = nome.split()
ultimo_nome = len(lista_nomes) - 1
print("O seu primeiro nome é:", lista_nomes[0])
print("O seu último nome é:", lista_nomes[-1])