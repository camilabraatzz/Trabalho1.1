# Faça um Programa que peça um número e informe se o número é inteiro ou decimal.

num = float(input('Digite um número: '))

if num == round(num):
        print("Inteiro")
else:
        print("Decimal")