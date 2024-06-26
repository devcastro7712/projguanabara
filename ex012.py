#Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
preco = float(input("qual o preço do produto?"))
desconto = preco * 5 / 100
precoFinal = preco - desconto
print("O novo preço do produto é de R${}".format(precoFinal))