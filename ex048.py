somaidd = 0
mediaidd = 0
homemvelho = 0
nomevelho = ''
totmulher20 = 0
for p in range(1,5):
    print('--------- {}° PESSOA--------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidd += idade
    if  p == 1 and sexo in 'Mm':
        homemvelho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > homemvelho:
        homemvelho = idade
        nomevelho = nome
    if sexo in 'Ff' and idade  < 20:
        totmulher20 += 1
mediaidd = somaidd / 4
print('A média do grupo é {} anos'.format(mediaidd))
print( 'O homem mais velho tem {} anos e se chama {}'.format(homemvelho , nomevelho))
print(' O Número de mulher com menos de 20 anos é: {}'.format(totmulher20))

