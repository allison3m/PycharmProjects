x = soma = cont = maior = menor = 0
while x != 'N':
    cont += 1
    num = int(input('Digite um número:'))
    soma += num
    media = soma / cont
    if num > maior or maior == 0:
        maior = num
    if num < menor or menor == 0:
        menor = num
    x = str(input('Quer continuar:(S/N)')).strip()[0].upper()
print('A média dos números digitados é {} seu maior é {} e seu menor é {}.'.format(media, maior, menor))