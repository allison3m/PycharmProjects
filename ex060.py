cont = soma = 0
while True :
    num = int(input('Digite um número [999 para finalizar]:'))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'Foram digitados {cont} números, e a soma deles são: {soma}')

