while True:
    num = int(input('Digite um valor para tabuada\n(número negativo para finalizar programa):'))
    if num < 0:
        break
    for c in range (1,11):
        print(f'{num} X {c} = {num * c}')
print('PROGRAMA ENCERRADO')