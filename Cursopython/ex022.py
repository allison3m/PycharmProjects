from random import shuffle
n1=str(input('1°Aluno:'))
n2=str(input('2°Aluno:'))
n3=str(input('3°Aluno:'))
n4=str(input('4°Aluno:'))
l=[n1,n2,n3,n4]
shuffle(l)
print('A Ordem de apresentação será:{}'.format(l))