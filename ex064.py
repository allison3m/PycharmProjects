cont = contf = contm = 0
print('###'*20)
print('                  FAÇA SEU CADASTRO')
print('###'*20)

while True:
    idd = int(input('Qual é sua idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual é seu sexo:[M/F]')).upper().strip()[0]
    if idd >= 18:
        cont += 1
    if sexo == 'M':
        contm += 1
    if sexo == 'F' and idd < 20:
        contf += 1
    pg = ' '
    while pg not in 'SN':
        pg = str(input('Quer continuar(S/N):')).upper().strip()[0]
    if pg == 'N':
        break
print(f'Temos {cont} pessoa(s) com mais de 18 anos ')
print(f'Temos {contm} homen(s) cadastrados ')
print(f'E Tem {contf} mulher(es) com menos de 20 anos, cadastradas ')









