nome = str(input('Qual é o seu nome completo? '))
nome1 = nome.strip().upper()
nome2 = nome.strip().lower()
separada = nome.split()
qntd1nome = separada[0]
qntd0 = int(len(separada[0]))
qntd1 = int(len(separada[1]))
qntd2 = int(len(separada[2]))
print(f'Nome em maiúsculo: {nome1}; \nNome em minúsculo: {nome2}.')
print('O seu primeiro nome possui {} letras.'.format(len(qntd1nome)))
print('O seu nome completo possui {} letras.'.format(qntd0+qntd1+qntd2))
