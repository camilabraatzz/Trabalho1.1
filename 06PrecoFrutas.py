# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade
# (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

def preco_maca(qt_kg):
    preco_total = 0
    if qt_kg <= 5:
        preco_total = qt_kg * 2.50
    else:
        preco_total = qt_kg * 2.20
    if preco_total > 25:
        preco_total = preco_total - (preco_total * 10)/100
    return preco_total

def preco_morango(qt_kg):
    preco_total = 0
    if qt_kg <= 5:
        preco_total = qt_kg * 1.80
    else:
        preco_total = qt_kg * 1.50
    if preco_total > 25:
        preco_total = preco_total - (preco_total * 10)/100
    return preco_total


maca_kg = float(input('Digite a quantidade em kg de maçãs desejadas '))
valor_total = preco_maca(maca_kg)
print('O valor a ser pago é de: ', valor_total)

morango_kg = float(input('Digite a quantidade em kg de morangos desejados '))
valor_total = preco_morango(morango_kg)
print('O valor a ser pago é de: ', valor_total)
