from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pes in range(1,8):
    nasc = int(input('Em que ano a {}° pessoa nasceu?'.format(pes)))
    idade = atual - nasc
    if idade >= 18:
       totmaior += 1
    else:
        totmenor += 1
print('Ao todos são {} pessoas maiores de idade e {} pessoas menores'.format(totmaior , totmenor))





