#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
#pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias = float(input("quantos dias alugados?"))
km = float(input("quantos Km rodados?"))
precoDia = dias * 60
precoKm = km * 0.15
total = precoKm + precoDia


print("O preço a pagar será de R${:.2f}".format(total))