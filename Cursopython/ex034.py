casa = float(input('Qual o valor da casa:'))
salario = float(input('Qual seu salário:'))
ano = int(input('Quantos anos gostaria de pagar:'))
dividendo = ano * 12
prestacao = casa / dividendo
limite = salario * 0.30
if prestacao > limite :
    print( 'Você não poderá efetuar o empréstimo, devido limite excedido!')
elif prestacao < limite :
    print('Parabéns, sua prestação será de R${:.2f}!!'.format(prestacao))
print('Tenha um Bom dia!!!')

