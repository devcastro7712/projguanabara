#O mesmo professor do desafio anterior quer sortear a ordem de apresenteção do trabalho dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
import random
lista = ["lucas", "sérgio", "andré", "bruno"]
random.shuffle(lista)
print("a nova ordem de será a seguinte: {}".format(lista))