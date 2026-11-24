lista_catalogo = []

for i in range(3):
    print(f'\nContato #{i+1}')
    contato= {}

    contato['nome'] = input('Informe o nome completo: ')
    contato['telefone'] = int(input('Informe o numero de contato: '))
    contato['email'] = input('Informe o seu e-mail: ')

    lista_catalogo.append(contato)
# print(lista_catalogo)

for elemento in lista_catalogo: # 3 vezes
    print(f'\nNome: {elemento['nome']}')
    print(f'telefone: {elemento['telefone']}')
    print(f'email: {elemento['email']}')