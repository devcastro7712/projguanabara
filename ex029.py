# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada km acima do limite.

velocidade = int(input("Em qual velocidade o carro estava?\n"))
custo = 7

if velocidade > 80:
    multa = (velocidade - 80) * custo
    print("Você ultrapassou {}km/h a velocidade permitida e pagará R${} de multa!\n".format(velocidade - 80, multa))
else:
    print("Você estava dentro da velocidade permitida!\n")
