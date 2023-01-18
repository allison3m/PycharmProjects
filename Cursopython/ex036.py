num1 = float((input('Digite um numéro:')))
num2 = float(input('Digite outro número:'))
maior = num1 > num2
menor = num1 < num2
igual = num1 == num2
if maior :
    print('O primeiro número {} é maior que o {}'.format(num1 , num2))
elif menor :
    print('O seu primeiro número {} é menor que o {}'.format(num1 , num2))
elif igual :
    print('O seu primeiro número {} é igual ao segundo {}'.format(num1 , num2))
