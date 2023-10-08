#Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
medida = float(input("Insira o valor em metros: "))
quilometros = medida/1000
centimetros = medida*100
milimetros = medida*1000
decametros = medida/10
decimetros = medida/0.10
print("=" * 20)
print("CONVERSOR DE MEDIDAS")
print("=" * 20)
print(f"{medida} m = {quilometros} Km")
print(f"{medida} m = {decametros} dam")
print(f"{medida} m = {centimetros} cm")
print(f"{medida} m = {milimetros} mm")
print(f"{medida} m = {decimetros} dm")
