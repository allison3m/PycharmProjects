soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('A soma dos {} termos ímpares e divisivis por 3 que estão entre 1 a 500 é: {}'.format(cont, soma))
