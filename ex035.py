# Desenvolva um programa que leia o comprimento de três retas e diga se ele pode ou não formar um triângulo.

reta1 = float(input("Qual o tamanho da reta maior?"))
reta2 = float(input("Qual tamanho da segunda reta?"))
reta3 = float(input("Qual o tamanho ta terceira reta"))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print("as três retas formam um triângulo")
else:
    print("As três retas não formam um triângulo")