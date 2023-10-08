#Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
real = float(input("Insira quanto dinheiro você tem na carteira em reais: "))
dolar = real/4.86
print(f"Você pode comprar US${dolar:.2f} dólares com R${real:.2f}")
