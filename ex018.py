#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math

angulo = float(input("me dê um ângulo"))
ang = math.radians(angulo)
sin = math.sin(ang)
cos = math.cos(ang)
tan = math.tan(ang)

print(
    "você me deu um ângulo de {:.2f}°\nseu seno é de {:.2f}°\nseu cosseno é de {:.2f}ª\ne sua tangente de {:.2f}°".format(angulo, sin, cos, tan)
)