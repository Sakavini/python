primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))
terceiro_numero = int(input("Digite o terceiro número: "))

if primeiro_numero > segundo_numero and primeiro_numero > terceiro_numero:
    print(f"O maior número é: {primeiro_numero}")
elif segundo_numero > primeiro_numero and segundo_numero > terceiro_numero:
    print(f"O maior número é: {segundo_numero}")
elif terceiro_numero > primeiro_numero and terceiro_numero > segundo_numero:
    print(f"O maior número é: {terceiro_numero}")
else:
    print("Todos os números são iguais")