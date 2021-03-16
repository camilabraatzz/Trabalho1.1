# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar; positivo ou negativo; inteiro ou decimal.

def operacoes(num1, num2, operador):
    if operador == '+':
        operacao = num1 + num2
    elif operador == '-':
        operacao = num1 - num2
    elif operador == '*':
        operacao = num1 * num2
    elif operador == '/':
        operacao = num1 / num2
    else:
        print('Você não escolheu nenhuma operação, tente novamente!')

    return operacao


numero1 = int(input('Digite o primeiro número '))
numero2 = int(input('Digite o segundo número '))
operador = input('Escolha a operação desejada: soma(+), subtração(-), multiplicação(*) ou divisão(/) ')

resultado = operacoes(numero1, numero2, operador)
print('O resultado da operação é: ', resultado,)

if resultado % 2 == 0:
    print('O número é par')
else:
    print('O número é ímpar')

if resultado < 0:
    print('O número é negativo')
else:
    print('O número é positivo')

print(type(resultado))