letra = input("Digite uma letra para saber se é vogal ou consoante: ")
x = letra.lower() # Lower retorna string em minuscula

if x.lower() in "aeiou":
    print(f"A letra {x} é uma vogal")
elif x.isalpha() and len(x) == 1: # isalpha verifica se é uma letra do alfabeto e len retorna o numero de itens
    print(f"A letra {x} é uma consoante")
else:
    print("Entrada inválida. Digite apenas uma letra!")