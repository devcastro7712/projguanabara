# Identifique as caracteristicas de um objeto
a = input("digite algo")

print("O tipo primito desse valor é {}".format(type(a)))
print("Só tem espaços? {}".format(a.isspace()))
print("É um número? {}".format(a.isnumeric()))
print("É alfabético? {}".format(a.isalpha()))
print("É alfanumérico? {}".format(a.isalnum()))
print("Está em maiúsculo? {}".format(a.isupper()))
print("Está em minusculo? {}".format(a.islower()))
print("Está captalizado? {}".format(a.istitle()))
