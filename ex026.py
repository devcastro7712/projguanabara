# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a ultima vez.

nome = input("Me diga seu nome")
letra = input("qual letra você quer achar?")
nome = nome.upper()
letra = letra.upper()
nome = nome.count(letra)
print("No seu nome tem {} letras {}".format(nome, letra))