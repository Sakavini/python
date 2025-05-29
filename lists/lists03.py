numeros = []

for i in range(3):
    numero = float(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

invertida = numeros[::-1]

print(f"Lista invertida: {invertida}")