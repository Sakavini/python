try:
    primeiro_numero = int(input("Digite o primeiro número: "))
    segundo_numero = int(input("Digite o segundo número: "))
    resultado = primeiro_numero / segundo_numero
except ValueError:
    print("Por favor, digite um número válido")
except ZeroDivisionError:
    print("Erro, não aceitamos divisões por zero")
else:
    print(f"A divisão entre {primeiro_numero} e {segundo_numero} é: {resultado}")
finally:
    print("Programa finalizado")