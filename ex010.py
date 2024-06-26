#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
d = float(input("quanto você tem na carteira hoje?"))
dolar = 5.45
converted = d / dolar
print("com esse valor você poderia comprar {:.2f} dolares".format(converted))