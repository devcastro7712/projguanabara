#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
num = int(input("Digite um número"))
ant = num - 1
suc = num + 1

print("Voçê digitou o número {}, o antecessor desse número é: {} e o sucessor é: {}".format(num, ant, suc))