# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input("me dê um número"))
n2 = int(input("me dê um número"))
n3 = int(input("me dê um número"))

maior = max(n1, n2, n3)
menor = min((n1, n2, n3))

print("O maior número da lista é {}".format((maior)))
print("O menor número da lista é {}".format(menor))