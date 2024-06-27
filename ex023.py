# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
# Ex: digitando o número 1234
# Unidade: 4
# Dezena: 3
# Centena: 2
# Milhar: 1

num = (input("Digite um número"))

und = num[-1]
print("Unidade: {}".format(und))
dez = num[-2]
print("Dezena: {}".format(dez))
cen = num[-3]
print("Centena: {}".format(cen))
mil = num[-4]
print("Milhar: {}".format(mil))
