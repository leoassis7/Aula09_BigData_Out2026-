lista_catalogo = []

for i in range(2):
    print(f'\nLivro #{i+1}')
    livro= {}

    livro['título'] = input('Informe o nome do Livro: ')
    livro['autor'] = input('Informe o nome do autor: ')
    livro['ano'] = int(input('Informe o ano de publicação: '))
    livro['genero'] = input('Informe o genero: ')
    livro['paginas'] = int(input('Informe o numero de páginas: '))

    lista_catalogo.append(livro)
print(lista_catalogo)

for elemento in lista_catalogo: # 3 vezes
    print(elemento)
    if elemento['ano'] >= 2020:
        print(elemento)
