try:
    numero = int(input("Digite um número: "))
except ValueError:
    print("Por favor, digite um número válido")
else:
    print(f"Você digitou o número {numero}")
finally:
    print("Programa finalizado")