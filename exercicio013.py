#Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input("Insira o valor do salário: R$ "))
salario_reajustado = salario + (salario*0.15)
print(f"O valor do salário reajustado em 15% é R$ {salario_reajustado:.2f}")