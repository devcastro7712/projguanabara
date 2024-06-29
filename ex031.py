# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem.
# cobrando R$0,50 por Km para viagens até 200Km e R$0,45 para viagens mais longas.

distancia = int(input("Quantos Km foram rodados?\n"))
vlongas = 0.45
vcurtas = 0.50
if distancia <= 200:
    passagem = distancia * vcurtas
    print("Como distancia foi de {}km, será cobrado R$0,50 por Km, logo você pagará R${}".format(distancia, passagem))
else:
    passagem = distancia * vlongas
    print("Como distancia foi de {}km, será cobrado R$0,45 por Km, logo você pagará R${}".format(distancia, passagem))
