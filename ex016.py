#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
#EX: Digite um número: 6,127 e apareça apenas seu inteiro que é 6.

from math import trunc

num = float(input("me dê um número real"))

print("O inteiro do número {} é {}".format(num, trunc(num)))

