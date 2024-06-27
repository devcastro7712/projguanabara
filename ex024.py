# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "SANTO"

cidade = input("Me dê o nome de uma cidade").strip()

if cidade[:5].upper() == "SANTO":
    print("A palavra começa com SANTO")
else:
    print("A palavra não começa com SANTO")
