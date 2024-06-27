# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = input("Qual seu nome completo?")
nome = nome.strip()
nome = nome.upper()

if "SILVA" in nome:
    print("Você tem SILVA no nome!")
else:
    print("Você não tem SILVA no nome")