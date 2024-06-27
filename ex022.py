# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas as letras minusculas
# Quantas letras ao todo (sem considerar os espaços)
# quantas letras tem o primeiro nome

nome = str(input("Qual é o seu nome?")).strip()
print("Seu nome em maiusculo é {}".format(nome.upper()))
print("Seu nome em minusculo é {}".format(nome.lower()))
print("Seu nome ao todo tem {} letras".format(len(nome) - nome.count(" ")))
print("Seu primeiro nome tem {} letras".format(nome.find(" ")))
