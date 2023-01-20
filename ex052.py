m = 0
x = 0
while m != 5:
    n1 = int(input('Digite um valor:'))
    n2 = int(input('Digite outro valor:'))
    print('ESCOLHA UMA MÉTODO DE CALCULO:\n[ 1 ] somar\n[ 2 ] multiplicar \n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa)')
    m = int(input('Digite o número:'))
    if m == 1 :
        x = n1 + n2
        print(x)
    elif m == 2 :
        x= n1 * n2
        print(x)
    elif m == 3 :
        if n1 > n2:
            print(f'O número maior é {n1}')
        elif n1 == n2:
            print(f'O números {n1} e {n2} são iguais')
        else:
            print(f'O número {n1} é menor que o {n2}')
print('Obrigado, por participar!')
