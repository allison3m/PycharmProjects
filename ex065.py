totalp =  cont1000 = menor = cont = 0
barato = ''
while True:
    n = str(input('Qual nome do produto:'))
    p = float(input('Qual o preço:'))
    cont += 1
    pg = ' '
    totalp += p
    if p > 1000:
        cont1000 += 1
    if cont == 1 or p < menor:
        menor = p
        barato = n
    while pg not in 'SN':
        pg = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if pg == 'N':
        break
print(f'A soma de todos os preços é R$ {totalp:.2f}.')
print(f'temos {cont1000} produto(s) custando mais de R$ 1000.00 .')
print(f'O produto mais barato é o(a) {barato} e custa R$ {menor:.2f} .')

