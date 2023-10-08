#Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
produto = float(input("Insira o valor do produto: R$ "))
produto_desconto = produto - (produto*0.05)
print(f"Valor do produto com desconto de 5%: R${produto_desconto:.2f}")
