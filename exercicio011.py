#Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
print("="*20)
print("CALCULADORA DE TINTA")
print("="*20)
largura = float(input("Insira a largura da parede: "))
altura = float(input("Insira a altura da parede: "))
area = largura*altura
litros_tinta = area/2
print(f"Para uma área de {area:.1f}m² você precisará de {litros_tinta:.1f} litros de tinta")
