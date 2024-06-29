# Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu

import random

numero = random.randint(0, 5)
escolha = int(input("Me dê um número entre 0 e 5\n"))
if numero == escolha:
    print("Você acertou, o número que pensei foi o número {}".format(numero))
else:
    print("Você errou, eu pensei no número {}".format(numero))
