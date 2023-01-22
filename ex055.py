p1= int(input('Qual primeiro termo:'))
r = int(input('Qual a razão:'))
termo = p1
cont = 1
while cont <= 10:
    print('{} → '.format(termo),end= '')
    cont += 1
    termo += r
print('FIM')