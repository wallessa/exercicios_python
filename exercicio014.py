#Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
temp_celsius = float(input("Insira a temperatura em ºC: "))
temp_fahrenheit = (temp_celsius * 1.8) + 32
print(f"Temperatura em Fahrenheit: {temp_fahrenheit:.1f}ºF")