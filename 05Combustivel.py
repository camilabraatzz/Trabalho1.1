# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
# (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor
# a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$
# 2,50 o preço do litro do álcool é R$ 1,90.

def preco_combustivel(qt_litros, tipo_combustivel):
    preco_alcool = 1.90
    preco_gasolina = 2.50
    preco_total = 0
    if str.upper(tipo_combustivel) == 'A':
        sub_total = qt_litros * preco_alcool
        if qt_litros <= 20:
            preco_total = sub_total - (sub_total * 3) / 100
        else:
            preco_total = sub_total - (sub_total * 5) / 100
    elif str.upper(tipo_combustivel) == 'G':
        sub_total = qt_litros * preco_gasolina
        if qt_litros <= 20:
            preco_total = sub_total - (sub_total * 4) / 100
        else:
            preco_total = sub_total - (sub_total * 6) / 100
    else:
        print('Você não escolheu nenhum tipo!')

    return preco_total


litros = float(input('Digite a quantidade de litros vendidos '))
combustivel = input('Digite o tipo de combústivel desejado. A para Álcool e G para Gasolina ')

valor_total = preco_combustivel(litros, combustivel)
print('O valor a ser pago é de: ', valor_total)
