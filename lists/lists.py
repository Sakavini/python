# Listas são estruturas de dados em Python que armazenam vários valores em uma única variável.
# Elas podem conter elementos de diferentes tipos (números, strings, etc.) e permitem acesso, modificação e iteração sobre seus itens.

numeros = []

for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

soma = sum(numeros)
print(f"A soma dos números é: {soma}")