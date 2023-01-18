p1 = int(input('Digite o primeiro termo:'))
r = int(input('Digite a razão da PA:'))
d = p1 + (10 - 1) * r
for c in range(p1, d + 1, r): # o +1 é pq o python começa contar do 0
    print('{}'.format(c), end = ' → ')
print('Fim')