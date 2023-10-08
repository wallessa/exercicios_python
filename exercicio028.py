#Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
import time
print("="*40)
print("           JOGO DA ADIVINHAÇÃO")
print("="*40)
num = int(input("Pense e digite um número entre 0 e 5: "))
print("...")
time.sleep(3)
ganhador = random.randint(0,5)
print(f"E o número sorteado foi: {ganhador}")
if num == ganhador:
    print("Parabéns, você ganhou!")
else:
    print("Não foi dessa vez, você perdeu...")
