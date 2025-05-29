# Tratamento de erros é uma técnica usada para lidar com situações inesperadas que podem causar falhas no programa, como entradas inválidas ou problemas de conexão.

# Em Python, usamos blocos try, except, else e finally para capturar e tratar esses erros, evitando que o programa pare de funcionar abruptamente.
# Isso torna o código mais robusto e confiável.

# No seu exemplo, o tratamento de erros impede que o programa quebre se o usuário digitar algo que não seja um número.

try:
    numero = int(input("Digite um número: "))
except ValueError:
    print("Por favor, digite um número válido")
else:
    print(f"Você digitou o número {numero}")
finally:
    print("Programa finalizado")