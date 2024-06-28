print("Opções:")
print("1. Adicionar produto")
print("2. Verificar estoque")
print("3. Remover produto")
print("4. Sair")

escolha = input("Escolha uma opção (1, 2, 3 ou 4): ")

produto = []
quantidade = []

while escolha != '4':
    if escolha == '1':
        produto.append(input("Digite o nome do produto: "))
        quantidade.append(int(input("Digite a quantidade: ")))
        print("Produto adicionado com sucesso!")
    elif escolha == '2':
        quantidadeEstoque = sum(quantidade)
        print(f"Quantidade total em estoque: {quantidadeEstoque}")
    elif escolha == '3':
        itemRemovido = input(f"Produtos: {produto}\nDigite o nome do produto que deseja excluir: ")
        if itemRemovido in produto:
            produto.remove(itemRemovido)
            print(f"{itemRemovido} removido com sucesso!")
        else:
            print(f"{itemRemovido} não encontrado na lista de produtos.")
    else:
        print("Opção inválida. Escolha novamente.")

    escolha = input("Escolha uma opção (1, 2, 3 ou 4): ")

print("Fim")
