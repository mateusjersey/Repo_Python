# # lista_produto = ["ipad", 'iphone', 'airpod' ,'macbook']
# # preco = ['3000', '5000','800','10000']

# # print(lista_produto[0])

# dic_produto = {'ipad': 3000, 'iphone': 5000, 'airpod': 800 , 'macbook': 10000}

# print(dic_produto)

# # Encontrar valor no dicionário
# print(dic_produto['ipad'])

# # Adicionar valor no dicionário
# dic_produto['airpod'] = 2000
# dic_produto['apple whatch'] = 8000
# print(dic_produto)

# # Calcular valor dentro do dicionário

# dic_produto['iphone'] = dic_produto['iphone'] * 1.3
# print(dic_produto)

# #Remover valor da lista
# dic_produto.pop('apple whatch')
# print(dic_produto)

# #Adicionar valor
# dic_produto['apple whatch'] = 8000
# print(dic_produto)

# #Verificador de produto
# if 'poco f5' in dic_produto:
#     print('O produto existe')
# else:
#     print("O produto não existe")

# #verificador pelo valor
# if 15000 in dic_produto.values():
#     print("Existe um produto com esse valor"
#     )
# else:
#     print('Não existe produto com esse valor')

# # cadastro de produto e preço no dicionário
# dic_produto['poco x3'] = 1000
# print(dic_produto)
# # Atualizem o valores dos produtos com um aumento de 50%

# for produto in dic_produto:
#     dic_produto[produto] = dic_produto[produto] * 1.5
# print(dic_produto)



meus_produtos = {"mouse": 150,"teclado": 200,"monitor": 800,"gabinete": 500 }

# Mostre todos os produtos e seus preços.
print(meus_produtos)
# Peça ao usuário o nome de um produto e mostre o preço (se existir no dicionário).
# buscar_produto = input("Digite um produto: ")
# if buscar_produto in meus_produtos:
#     print(f'O produto é {buscar_produto} e o valor é', meus_produtos[buscar_produto])
# else:
#     print("Podruto não existe")
# Peça o nome de um produto e um novo preço, e atualize o valor no dicionário.
# nome_produto = input("Digite um produto: ")
# novo_valor = float(input("Digite o novo valor do produto: "))

# meus_produtos[nome_produto] = novo_valor
# print(meus_produtos)


# Permita que o usuário adicione um novo produto com seu preço ao dicionário.
# novo_produto = input("Digite um novo produto: ")
# valor_produto = float(input("Digite o valor do novo produto: "))

# meus_produtos[novo_produto] = valor_produto
# print(meus_produtos)
# Solicite o nome de um produto e remova-o do dicionário (caso exista).
# remover_produto = input("Digite o produto para remover: ").lower()
# if remover_produto in meus_produtos:
#     meus_produtos.pop(remover_produto)
#     print(meus_produtos)
# else:
#     print("Produto não existe")


# Crie um novo dicionário com 10% de desconto aplicado em todos os preços.

for produto in meus_produtos:
    meus_produtos[produto] = meus_produtos[produto] *0.9
print(meus_produtos)