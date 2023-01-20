from random import randint
c = randint(0, 10)
acertou = False
palpites = 0
print('Tente adivinhar um número de 0 a 10...')
while not acertou:
    num = int(input('Qual é seu palpite:'))
    palpites += 1
    if num == c :
        acertou = True
    else:
        if num < c :
            print('Mais... tente novamente!')
        else:
            print('Menos ... tente novamente!')
print('Acertou com total de {} palpites!'.format(palpites))