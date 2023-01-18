from random import choice
a= str(input('Primeiro Nome:'))
b= str(input('Segundo Nome:'))
c=str(input('Terceiro nome:'))
d=str(input('Quarto nome:'))
lista=[a,b,c,d]
escolhido=choice(lista)
print('O aluno escolhido foi:{}'.format(escolhido))
