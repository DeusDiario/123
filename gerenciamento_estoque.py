tabela = {
    "Alface": {"preco": 5.00, "estoque": 10},
    "Batata": {"preco": 4.55, "estoque": 10},
    "Tomate": {"preco": 9.80, "estoque": 10},
    "Feijão": {"preco": 7.30, "estoque": 10}
}

valor_total = 0

while True:
    produto = input("Qual o produto? (ou digite 'Sair' para encerrar) ").capitalize()
    
    if produto == "Sair":
        print("Bye!")
        break
    
    if produto not in tabela:
        adicionar = input(f"O produto '{produto}' não está disponível. Deseja adicioná-lo ao estoque? (s/n) ").lower()
        if adicionar == 's':
            preco = float(input("Digite o preço do produto: "))
            estoque = int(input("Digite a quantidade do produto: "))
            tabela[produto] = {"preco": preco, "estoque": estoque}
            print(f"Produto '{produto}' adicionado com sucesso!")
        else:
            continue
    
    quantidade = int(input("Quantidade: "))
    
    # Verifica se há estoque suficiente
    if quantidade > tabela[produto]["estoque"]:
        adicionar_1 = input(f"Desculpe, não há quantidade suficiente de '{produto}' em estoque. Gostaria de adicioná-lo? (s/n)")
        if adicionar_1 == 's':
         preco = float(input("Digite o novo preço do produto: "))
         estoque = int(input("Digite a nova quantidade do produto: "))
         tabela[produto] = {"preco": preco, "estoque": estoque}
        print(f"Estoque disponível: {tabela[produto]['estoque']}")
        continue
    
    # Atualiza o estoque e calcula o valor da compra
    valor_produto = tabela[produto]["preco"] * quantidade
    valor_total += valor_produto
    tabela[produto]["estoque"] -= quantidade
    print(f"Você comprou {quantidade} de '{produto}' por R${valor_produto:.2f}.")
    print(f"Estoque restante de '{produto}': {tabela[produto]['estoque']}")

print(f"Valor total das compras foi de: R${valor_total:.2f}")
