# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input("me de um ano"))

if ano % 4 == 0 and ano % 100 != 0 and ano % 400 == 0:
    print("O ano {} é um ano bissexto".format(ano))
else:
    print("O ano {} não é um ano bissexto".format(ano))