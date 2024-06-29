# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Qual o salário atual do funcionário?"))
if salario > 1250.00:
    maiorsalario = (salario * 10 / 100) + salario
    print("O salário que era de R${} foi ajustado em 10% e ficou em R${}".format(salario, maiorsalario))
else:
    menorsalario = (salario *15 / 100) + salario
    print("O salário que era de R${} foi ajustado em 15% e ficou em R${}".format(salario, menorsalario))