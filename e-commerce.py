produtos ={'Produto A': 300, 'Produto B': 80, 'Produto C': 60,
 'Produto D': 200, 'Produto E': 250, 'Produto F': 30}

vendas_produtos = list(produtos.values())
nomes_produtos = list(produtos.keys())

total_de_vendas = sum(vendas_produtos)

mais_vendido = max (produtos, key=produtos.get)

print(f"O total de vendas é igual a {total_de_vendas} e o item mais vendido foi o {mais_vendido}.")

