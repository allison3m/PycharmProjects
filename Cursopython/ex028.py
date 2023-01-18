frase = str(input('Escreva uma frase:')).upper().strip()
print('Sua frase contém {} letra(s) A  . '.format(frase.count('A') ))
print ('A primeira letra A aparece primeiro na {}º letra'.format(frase.find('A')+1))
print ('A ultima letra A aparece na {}° letra'.format(frase.rfind('A')+1))