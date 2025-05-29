nomes = []

quantidade = int(input("Digite quantos nomes você quer digitar: "))

for i in range(quantidade):
    nome = input(f"Digite o {i + 1}º nome: ")
    nomes.append(nome)

busca = input("Digite o nome que deseja buscar: ")

if busca in nomes:
    posicao = nomes.index(busca)
    print(f"O nome '{busca} está na lista, na posicão {posicao}.")
else:
    print(f"O nome {busca} não foi encontrado na lista.")