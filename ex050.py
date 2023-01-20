s = 0
while s != 'M' and s != 'F':
   s = str(input('Qual seu sexo:[M/F]')).upper().strip()
   if s != 'M' and s != 'F':
      print('Dados Inválidos, Por favor, informe seu sexo:')
print(f'Sexo {s} registrado com sucesso!')