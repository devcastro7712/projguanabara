#Um professor quer sortear um dos alunos para apagar o quadro. Faça um programa que ajude ele lendo o nome deles e escrevendo
#um nome na tela
import random

lista = ("lucas", "sérgio", "andré", "bruno")


print("o aluno sorteado foi {}".format(random.choice(lista)))

