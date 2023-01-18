velocidade = float(input('Escreva sua velocidade :'))
multa = (velocidade-80) * 7
if velocidade > 80:
    print('VOCÊ FOI MULTADO NO VALOR DE R$ {:.2f} , POR ATINGIR O LIMITE DA VIA DE 80 Km/h'.format(multa))
else:
    print('Tenha um bom dia, Dirija com segurança!')