#Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
cidade = input("Insira o nome da cidade: ").strip()
print(cidade[:5].lower() == "santo")

