#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
num = int(input("Digite um número"))
dobro = num * 2
triplo = num * 3
raiz = num ** 0.5
print("Você digitou o número: {}, seu dobro é: {}, seu triplo é: {} e sua raiz quadrada é: {:.2f}".format(num, dobro, triplo, raiz))
