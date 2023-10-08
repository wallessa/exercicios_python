#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
quilometros = float(input("Qual a quantidade de quilômetros percorridos pelo carro alugado? "))
dias = int(input("Por quantos dias o carro foi alugado? "))
pagamento = (dias*60) + (quilometros*0.15)
print(f"Valor a pagar pela locação = R$ {pagamento:.2f}")