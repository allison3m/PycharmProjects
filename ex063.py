import random
print('-_' * 20)
print('        JOGO DE PAR OU IMPAR')
print('-_' * 20)
par = impar = soma = cont = 0
while True:
    pc = random.randint(0,10)
    num = int(input('Digite um número:'))
    pi = ' '
    while pi not in 'PI':
        pi = str(input('Você quer par ou ímpar [P/I]:')).upper().strip()[0]
    print(f'O pc escolheu {pc} e você {num}')
    if (pc + num) % 2 == 0:
        if pi == 'P':
            print(f'{pc} + {num} é {pc + num} e {pc + num} é Par.')
            print('Você ganhou!!!')
            cont += 1
        else:
            print(f'{pc} + {num} é {pc + num} e {pc + num} é Impar.')
            print('Você Perdeu!!!')
            break
    elif (pc + num) % 2 != 0:
        if pi == 'I':
            print(f'{pc} + {num} é {pc + num} e {pc + num} é Impar.')
            print('Você ganhou!!!')
            cont += 1
        else:
            print(f'{pc} + {num} é {pc + num} e {pc + num} é Impar.')
            print('Você Perdeu!!!')
            break
print(f'Você ganhou {cont} vez(es) do computador!')
