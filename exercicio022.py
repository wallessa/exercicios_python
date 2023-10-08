#Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.
nome = str(input("Insira seu nome: "))
print("Seu nome com letras maiúsculas: ", nome.upper())
print("Seu nome com letras minúsculas: ", nome.lower())
tamanho_nome = len(nome.replace(" ",""))
print(f"Quantidade de caracteres do nome: {tamanho_nome}")
lista_nomes = nome.split()
print("Quantidade de letras do primeiro nome:", len(lista_nomes[0]))

