#Faça um algoritmo que leia o salário de um funcinário e mostre seu novo salário, com 15% de aumento.
salario = float(input("qual o salário do funcionário?"))
abono = salario * 15 / 100
reajuste = salario + abono

print("O novo salário do funcionário será de R${} após o reajuste".format(reajuste))