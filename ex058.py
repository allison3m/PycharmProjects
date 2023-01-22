num = cont = soma = 0
while num != 999:
    soma += num
    if soma != 0 :
        cont += 1
    num = int(input('Digite um número [ 999 para parar]:'))
print('Foram digitados {} numero(s) e a soma deles é {}'.format(cont, soma))
