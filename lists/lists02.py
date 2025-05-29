numeros = []

quantidade = int(input("Quantos números você quer digitar: "))

for i in range(quantidade):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

sem_duplicatas = list(set(numeros))

print(f"Lista sem duplicatas: {sem_duplicatas}")