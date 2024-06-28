print("Opções:")
print("1. Adicionar produto")
print("2. Verificar estoque")
print("3. Remover produto")
print("4. Sair")
escolha = input("Escolha uma opção (1, 2, 3 ou 4): ")

produto = [0]
quantidade = [0]
estoque = print(produto)

while produto:
    if escolha == '1':
        produto += input("Digite o nome do produto: ")
        quantidade += (input("Digite a quantidade: "))
        print("Produto adicionado com sucesso!")
        
    escolha = input("Escolha uma opção (1, 2, 3 ou 4):")
    if escolha == '1':
        produto += input("Digite o nome do produto: ")
        quantidade += (input("Digite a quantidade: "))
        print("Produto adicionado com sucesso!")
    if escolha == '2':
        quantidadeEstoque = sum(quantidade)
    if escolha == '3':
        itemRemovido = input("Produtos:" + produto + "\nDigite o nome do produto que deseja excluir:")
        produto.remove[itemRemovido] 
    if escolha == '4':
        produto == False
        print("Fim")
    
