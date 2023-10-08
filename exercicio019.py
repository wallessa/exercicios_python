#Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random
aluno1 = input("Insira o nome do aluno: ")
aluno2 = input("Insira o nome do aluno: ")
aluno3 = input("Insira o nome do aluno: ")
aluno4 = input("Insira o nome do aluno: ")
alunos = [aluno1, aluno2, aluno3, aluno4]
print("O aluno sorteado foi: ", (random.choice(alunos)))