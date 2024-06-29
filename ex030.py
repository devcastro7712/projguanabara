# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input("Me dê um número\n"))

if numero % 2 == 0:
    print("{} é um número par!\n".format(numero))
else:
    print("{} é um número ímpar!\n".format(numero))
