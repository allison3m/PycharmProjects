f = int(input('Digite um número para calcular sua fatorial:'))
c = f
f = 1
print('Calculando {}! = '.format(f) , end='')
while c > 0:
    print('{} '.format(c), end='')
    print(' x ' if c > 1 else ' = ', end = '')
    f *= c
    c-= 1
print('{}'.format(f))
