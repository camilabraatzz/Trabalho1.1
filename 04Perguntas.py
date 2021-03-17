r1 = int(input("Telefonou para a vítima? 1/Sim ou 0/Não: "))
r2 = int(input("Esteve no local do crime? 1/Sim ou 0/Não: "))
r3 = int(input("Mora perto da vítima? 1/Sim ou 0/Não: "))
r4 = int(input("Devia para a vítima? 1/Sim ou 0/Não: "))
r5 = int(input("Já trabalhou com a vítima? 1/Sim ou 0/Não: "))

soma_respostas = r1 + r2 + r3 + r4 + r5

if soma_respostas < 2:
    print('Inocente')
elif soma_respostas == 2:
    print('Suspeita')
elif 3 <= soma_respostas <= 4:
    print('Cúmplice')
elif soma_respostas == 5:
    print('Assassino')
