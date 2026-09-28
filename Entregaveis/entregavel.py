# Sistema de cadastro e análise de produtos

produtos = []

quantidade = int(input("Quantos produtos deseja cadastrar? "))

# Cadastro dos produtos
for i in range(quantidade):
    print(f"\n--- Produto {i + 1} ---")

    nome = input("Nome: ")
    preco = float(input("Preço: R$ "))
    categoria = input("Categoria: ")

    produto = {
        "nome": nome,
        "preco": preco,
        "categoria": categoria
    }

    produtos.append(produto)


# Filtragem por preço
preco_maximo = float(
    input("\nDigite o preço máximo para filtrar: R$ ")
)

produtos_filtrados = [
    produto
    for produto in produtos
    if produto["preco"] <= preco_maximo
]


# Ordenação crescente
produtos_crescente = sorted(
    produtos,
    key=lambda produto: produto["preco"]
)


# Ordenação decrescente
produtos_decrescente = sorted(
    produtos,
    key=lambda produto: produto["preco"],
    reverse=True
)


# Categorias únicas usando set
categorias = {
    produto["categoria"]
    for produto in produtos
}


# Lista de preços
precos = [
    produto["preco"]
    for produto in produtos
]


# Tupla com estatísticas
estatisticas = (
    min(precos),
    max(precos),
    sum(precos) / len(precos)
)


# Relatório final
print("\n" + "=" * 50)
print("RELATÓRIO FINAL")
print("=" * 50)

print(f"\nTotal de produtos cadastrados: {len(produtos)}")

print("\n--- Produtos cadastrados ---")

for produto in produtos:
    print(
        f"Nome: {produto['nome']} | "
        f"Preço: R$ {produto['preco']:.2f} | "
        f"Categoria: {produto['categoria']}"
    )


print("\n--- Produtos até o preço informado ---")

if produtos_filtrados:
    for produto in produtos_filtrados:
        print(
            f"{produto['nome']} - "
            f"R$ {produto['preco']:.2f} - "
            f"{produto['categoria']}"
        )
else:
    print("Nenhum produto encontrado.")


print("\n--- Preços em ordem crescente ---")

for produto in produtos_crescente:
    print(
        f"{produto['nome']}: "
        f"R$ {produto['preco']:.2f}"
    )


print("\n--- Preços em ordem decrescente ---")

for produto in produtos_decrescente:
    print(
        f"{produto['nome']}: "
        f"R$ {produto['preco']:.2f}"
    )


print("\n--- Categorias únicas ---")

for categoria in categorias:
    print(f"- {categoria}")


# Estatísticas
menor_preco, maior_preco, preco_medio = estatisticas

print("\n--- Estatísticas gerais ---")

print(f"Menor preço: R$ {menor_preco:.2f}")
print(f"Maior preço: R$ {maior_preco:.2f}")
print(f"Preço médio: R$ {preco_medio:.2f}")

print("\n" + "=" * 50)
print("Fim do programa")
print("=" * 50)