tabela_precos = {
    "Alface": 5.00,
    "Batata": 4.55,
    "Tomate": 9.80,
    "Feijão": 7.30 }

estoque = {
    "Alface": 10,
    "Batata": 15,
    "Tomate": 8,
    "Feijão": 20 }

def exibir_estoque():
    """Exibe o estoque atual de produtos"""
    print("\n----- ESTOQUE ATUAL -----")
    print("Produto      | Preço (R$) | Quantidade")
    print("-" * 40)
    for produto, quantidade in estoque.items():
        if produto in tabela_precos:
            print(f"{produto:<12} | R$ {tabela_precos[produto]:<7.2f} | {quantidade}")
    print("-" * 40)

def adicionar_produto():
    """Adiciona um novo produto ao estoque"""
    nome = input("Nome do novo produto: ").capitalize()
    if nome in tabela_precos:
        print(f"Este produto já existe no estoque!")
        return
    
    try:
        preco = float(input("Preço do produto (R$): "))
        quantidade = int(input("Quantidade para o estoque: "))
        
        if preco <= 0 or quantidade < 0:
            print("Valores inválidos. O preço deve ser maior que zero e a quantidade não pode ser negativa.")
            return
            
        tabela_precos[nome] = preco
        estoque[nome] = quantidade
        print(f"\nProduto '{nome}' adicionado com sucesso ao estoque!")
    except ValueError:
        print("Erro: Insira valores numéricos válidos.")

def main():
    """Função principal do programa"""
    valor_total = 0
    carrinho = {}
    
    print("=== SISTEMA DE GERENCIAMENTO DE COMPRAS ===")
    print("Digite 'Sair' para finalizar as compras")
    print("Digite 'Estoque' para visualizar o estoque")
    print("Digite 'Adicionar' para incluir um novo produto\n")
    
    while True:
        produto = input("\nQual o produto? ").capitalize()
        
        if produto == "Sair":
            
            if carrinho:
                print("\nRESUMO DA COMPRA")
                for item, info in carrinho.items():
                    print(f"{item}: {info['quantidade']} x R$ {info['preco']:.2f} = R$ {info['subtotal']:.2f}")
                print(f"\nValor total das compras foi de: R${valor_total:.2f}")
            print("Obrigado pela preferência.")
            break
            
        elif produto == "Estoque":
            exibir_estoque()
            continue

        elif produto == "Adicionar":
            adicionar_produto()
            continue
            
        if produto not in tabela_precos:
            resposta = input(f"Produto '{produto}' não encontrado. Deseja adicionar ao estoque? (S/N): ")
            if resposta.upper() == "S":
                adicionar_produto()
            continue
            
        try:
            quantidade = int(input("Quantidade: "))
            if quantidade <= 0:
                print("A quantidade deve ser maior que zero.")
                continue
                
            if produto in estoque and quantidade <= estoque[produto]:
                valor_produto = tabela_precos[produto] * quantidade
                valor_total += valor_produto
                
                estoque[produto] -= quantidade
                
                if produto in carrinho:
                    carrinho[produto]['quantidade'] += quantidade
                    carrinho[produto]['subtotal'] += valor_produto
                else:
                    carrinho[produto] = {
                        'quantidade': quantidade,
                        'preco': tabela_precos[produto],
                        'subtotal': valor_produto
                    }
                
                print(f"Adicionado: {quantidade} x {produto} = R$ {valor_produto:.2f}")
                print(f"Subtotal: R$ {valor_total:.2f}")
            else:
                print(f"Estoque insuficiente. Disponível: {estoque.get(produto, 0)} unidades.")
        except ValueError:
            print("Por favor, digite um número válido para a quantidade.")

