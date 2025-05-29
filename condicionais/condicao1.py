# Condicionais são estruturas usadas em programação para tomar decisões com base em condições.


numero = int(input("Insira um número inteiro: "))

if numero > 0:
    print(f"O número {numero} é positivo")
elif numero < 0:
    print(f"O número {numero} é negativo")
else:
    print(f"O número {numero} é igual a 0")