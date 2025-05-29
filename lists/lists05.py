numeros = []

quantidade = int(input("Digite quantos números você quer digitar: "))

for i in range(quantidade):
    numero = float(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

busca = int(input("Digite o número que deseja buscar: "))

if busca in numeros:
    contador = numeros.count(busca)
    print(f"O número {busca} aparece {contador} vezes na lista")
else:
    print(f"O número {busca} não aparece na lista.")