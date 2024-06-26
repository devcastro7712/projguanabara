#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada
n = int(input("me dê um número"))

for i in range(11):
    print("{} x {:2} =".format(n, i), n * i)
