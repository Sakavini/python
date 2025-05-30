frutas = ("Morango", "Uva", "Banana", "Manga")

busca = input("Digite algum nome de fruta para buscar: ")

if busca in frutas:
    print(f"A fruta {busca} existe na tupla")
else:
    print(f"A fruta {busca} não existe na tupla")