from datetime import date #Alistamento Obrigatório
atual = date.today().year
nasc = int(input('Ano que nasceu:'))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem ou irá fazer {idade} anos.')
if idade == 18 :
    print('Esse é seu ano de Alistamento, procure a junta militar mais próxima.')
elif idade < 18 :
    print('Você ainda não completou 18 anos, falta(m) {} ano(s) que fazerá em {}'.format(18 - idade ,nasc + 18 ))
else :
    print('Se ainda não se alistou, procure a junta mais próxima e se regularize.')



