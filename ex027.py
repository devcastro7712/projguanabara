# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza
# Primeiro = Ana
# Último = Souza

nome = input("Qual seu nome completo?").strip()
nome = nome.title()
partenome = nome.split()

pnome = partenome[0]
unome = partenome[-1]

print("Seu primeiro nome é {} e seu último nome é {}".format(pnome, unome))


