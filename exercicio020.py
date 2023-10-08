#Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
aluno1 = input("Insira o nome do aluno: ")
aluno2 = input("Insira o nome do aluno: ")
aluno3 = input("Insira o nome do aluno: ")
aluno4 = input("Insira o nome do aluno: ")
alunos = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(alunos)
print(f"A ordem das apresentações será a seguinte: {alunos}")