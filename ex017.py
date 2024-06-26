#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo
#Calcule e mostre o comprimeiro da hipotenusa.

from math import hypot

catOp = float(input("qual o cateto oposto?"))
catAd = float(input("qual o cateto adjascente?"))
hipotenusa = hypot(catOp, catAd)
print("a hipotenusa é {:.2f}".format(hipotenusa))