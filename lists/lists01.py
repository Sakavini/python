numeros = []

quantidade = int(input("Quantos números você quer digitar: "))

for i in range(quantidade):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

maior = max(numeros)
menor = min(numeros)

print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")
