frase = str(input('Escreva a frase:')).strip().upper() # eliminação de espaços e subindo frase pra capslock
p = frase.split() # frase separada
tj = ''.join(p) # frase junta
i = ''
for l in range(len(tj)- 1, - 1, - 1):
    i += tj[l]
print(tj , "\033[31m|\033[m" , i)
if i == tj:
    print('O inverso de {} é {}'.format(tj, i))
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo')

