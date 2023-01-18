from math import sin,cos,tan,radians
a=float(input('Digite o ângulo que voce deseja calcular:'))
seno=sin(radians(a))
print('O ângulo {} tem o seno de {:.2f}'.format(a,seno))
cos=cos(radians(a))
tag=tan(radians(a))
print('O ângulo {} tem o cosseno de {:.2f}'.format(a,cos))
print('O ângulo {} tem o Tangente de {:.2f}'.format(a,tag))
