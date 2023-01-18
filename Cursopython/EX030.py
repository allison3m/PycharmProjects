from random import randint
pc = randint(0, 5) # PC PENSA NO NÚMERO
print('_=_' * 20 )
print('VOU PENSAR EM UM NÚMERO ENTRE 0 E 5, TENTE ADIVINHAR...')
print('_=_' * 20 )
user = int(input('Que número eu pensei?')) #USUARIO TENTA ADIVINHAR
print('PROCESSANDO....')
if pc == user:
    print('PARABÉNS VOCÊ ACERTOU!!!!')
else:
    print(f'Você errou eu pensei no número {pc} e não no {user}')



