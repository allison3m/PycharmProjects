l=float(input('Digite quantos metros de largura tem a sua parede:'))
h=float(input('Digite quantos metros de altura tem a sua parede:'))
a=l*h
print('Considerando o valor de {} m de largura e {} m de altura, logo sua área de pitura é {}m², \nportanto precisará de {} litros de tinta'.format(l,h,a,(a/2)))