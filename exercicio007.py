#Exercício Python 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
nome = str(input("Insira o nome do aluno: "))
nota1 = float(input("Insira a primeira nota do aluno: "))
nota2 = float(input("Insira a segunda nota do aluno: "))
media = (nota1+nota2)/2
print(f"A média do aluno {nome} é {media}.")