def dobro(a ):
    resultado = 2 * a
    # print(resultado)
    return resultado #Retorna o resultado para quem chamou

def triplo(a ):
    resultado = 3 * a
    # print(resultado)
    return resultado

def quadrado(a ):
    resultado = a ** 2
    # print(resultado)
    return resultado

# num1 = 5
# num2 = 9
# soma(num1, num2)


num1 = float(input('Informe o número: '))
    
dobro_num = dobro (num1)
triplo_num = triplo(num1)
quadrado_num = quadrado (num1)
     #Chamada da função
print(f'\nO dobro é:  {dobro_num}')
print(f'\nO triploé:  {triplo_num}')
print(f'\nO quadrado é:  {quadrado_num}')