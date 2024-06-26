#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
#de tinta necessária para pintá-la, sabendo que cada lata de tinta pinta uma área de 2m2

largura = float(input("qual a largura da parede?"))
altura = float(input("qual a altura da parede?"))
area = largura * altura
latas = area / 2

print("você tem uma parede de {} metros quadrados de área, para isso você precisará de {} latas de tinta".format(area, latas))