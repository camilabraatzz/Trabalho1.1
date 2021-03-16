resposta_sim = 0
perguntas = ['Telefonou para a vítima? ',
             'Esteve no local do crime? ',
             'Mora perto da vítima? ',
             'Devia para a vítima? ',
             'Já trabalhou com a vítima? ']

print(perguntas[0] + ' (S-sim ou N-não).')
resposta = input('Resp.:')
if resposta == 'S':
    resposta_sim += 1
print(perguntas[1] + ' (S-sim ou N-não).')
resposta = input('Resp.:')
if resposta == 'S':
    resposta_sim += 1
print(perguntas[2] + ' (S-sim ou N-não).')
resposta = input('Resp.:')
if resposta == 'S':
    resposta_sim += 1
print(perguntas[3] + ' (S-sim ou N-não).')
resposta = input('Resp.:')
if resposta == 'S':
    resposta_sim += 1
print(perguntas[4] + ' (S-sim ou N-não).')
resposta = input('Resp.:')
if resposta == 'S':
    resposta_sim += 1


if resposta_sim == 2:
    print('Suspeito')
elif resposta_sim == 3 and resposta_sim == 4:
    print('Cúmplice')
elif resposta_sim == 5:
    print('Assassino')
else:
    print('Inocente')