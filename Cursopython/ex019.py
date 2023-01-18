from math import sqrt
#from math import hypot
a=float(input('Digite o cateto adjacente:'))
b=float(input('Digite o cateto oposto:'))
h=sqrt(a**2+b**2)
print('Tendo em nota que o cateto adj é {} e o oposto é {}, logo a hipotenusa é:{:.2f}'.format(a,b,h))
                                                                                        #.format(a,b)