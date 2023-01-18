num = int(input('Digite um número inteiro:'))
print(''' Escolha uma base para conversão:
[1] Converter em BINÁRIO
[2] Converter em OCTAL
[3] Converter em HEXADECIMAL''')
base = int(input('sua opção:'))
if base == 1 :
    print(f'O valor {num} convertido em BINÁRIO é: {bin(num)[2:]}')
elif base == 2 :
    print(f'O valor {num} convertido em OCTAL é: {oct(num)[2:]}')
elif base == 3 :
    print(f'O valor {num} convertido em HEXADECIMAL é:{hex(num)[2:]}')
else:
    print('Opção inválida, tente novamente.')


