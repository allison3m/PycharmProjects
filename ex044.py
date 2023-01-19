t = 0
num = int(input('Digite um número inteiro e te direi se é um n° primo ou não:'))
for c in range(1 , num + 1):
    if num % c == 0:
        print('\033[34m', end='')
        t += 1
    else:
        print('\033[30m',end='')
    print('{}'.format(c), end= ' ')
print('\n\033[mO número {} foi divísivel {} vezes'.format(num, t))