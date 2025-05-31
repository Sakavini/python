dados = {
    "Nome": "João",
    "Idade": 20,
    "Cidade": "Campinas"
}

for chave, valor in dados.items():
    print(f"{chave}: {valor}")

# O método .items() em um dicionário retorna uma visão contendo pares de chave e valor. Ele permite percorrer o dicionário e acessar tanto a chave quanto o valor em cada iteração do laço for.