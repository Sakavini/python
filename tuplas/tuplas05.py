numeros = ()

for i in range(5):
    numero = int(input(f"Por favor, digite o {i + 1}º número: "))
    numeros += (numero,)

soma = sum(numeros)
print(f"A soma dos números é: {soma}")