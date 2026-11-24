produto = {} #Dicionario vazio

produto = {
    'nome': 'Notebook',
    'preco': 3500.80,
    'marca': 'Lenovo'
}

print(produto) #todas a chaves e valores
print(produto['nome']) #chaves e valores
print(produto['preco']) #todas a chaves e valores

# Alterando o valor
produto['marca'] = 'Positivo'
print(produto['marca'])

#Adicionando chaves
produto['tela'] = '18"'
print(produto)

#Deletando uma chave
del produto['marca']
print(produto)

print(produto.keys())
print(produto.values())
print(produto.items())
