primeiro_numero = int(input("digite um número: "))
segundo_numero = int(input("Digite outro número: "))

if primeiro_numero > segundo_numero:
    print(f"O maior número é: {primeiro_numero}")
elif segundo_numero > primeiro_numero:
    print(f"O maior número é: {segundo_numero}")
else:
    print(f"O número {primeiro_numero} e o número {segundo_numero} são iguais")