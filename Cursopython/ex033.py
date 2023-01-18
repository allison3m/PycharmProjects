nome = str(input('Qual é seu nome?'))
if nome == 'Allison':
    print('Que lindo nome você,tem Allison ❤')
elif nome == 'Lara' or nome == 'Lara Gabriela' or nome == 'lara' :
    print ('Você é a namorada do Allison, né?!')
elif nome in 'Jessica Natalia Janir Nivaldo':
    print('Você é parente do Allison, né?!')
else:
    print('Que nome mais normalzinho....')

print('Tenha um Bom dia, {}{}{}!!'.format('\033[4;34m' , nome , '\033[m'))
