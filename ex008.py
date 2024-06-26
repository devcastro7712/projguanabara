#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
valor = float(input("me dê um valor em metros"))
c = valor * 100
m = valor * 1000

print("{} metros equivalem a {} centímetros ou {} milímetros".format(valor, c, m))

