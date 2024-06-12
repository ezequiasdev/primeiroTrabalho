print("Opções:")
print("1. Adicionar produto")
print("2. Verificar estoque")
print("3. Remover produto")
print("4. Sair")
escolha = input("Escolha uma opção (1, 2, 3 ou 4): ")

produto = 0
quantidade = 0

produto1 = input("Digite o nome do produto: ")
produto2 = input("Digite o nome do produto: ")
produto3 = input("Digite o nome do produto: ")

estoque = (produto1, produto2, produto3)

for i in range(3):
    if escolha == "1":
        quantidade += int(input("Digite a quantidade: "))
        print("Produto adicionado com sucesso!")
escolha = input("Escolha uma opção (2, 3 ou 4):")
if escolha == "2":
    print("A quantidade de produtos é:", quantidade)
elif escolha == "3":
    print(F"Os produtos são: {estoque} e a quantidade é {quantidade}")
    input("Digite o produto que deseja remover: ")
    quantidade1 = int(input("Digite a quantidade que deseja remover: "))
    quantidade -= quantidade1
    print("Produto removido!")
elif escolha == "4":
    print("Saindo...")




