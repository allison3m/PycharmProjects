p1= int(input('Qual primeiro termo:'))
r = int(input('Qual a razão:'))
termo = p1
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} → '.format(termo),end= '')
        cont += 1
        termo += r
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais :'))
print('FIM')