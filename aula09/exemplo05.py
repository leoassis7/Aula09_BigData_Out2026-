def soma(a, b):
    resultado = a + b
    # print(resultado)
    return resultado #Retorna o resultado para quem chamou


# num1 = 5
# num2 = 9
# soma(num1, num2)

for i in range(3):
    num1 = float(input('Informe o número: '))
    num2 = float(input('Informe o número: '))
    r = soma(num1, num2) #Chamada da função
    print(r)