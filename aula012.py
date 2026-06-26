nome = str(input('Digite o seu nome: ')).upper()

if nome == 'GUSTAVO':
    print('{}, que nome lindo!'.format(nome))
elif nome == 'PEDRO' or nome == 'MARIA' or nome == 'PAULO':
    print('O seu nome é bem popular em Brasil, {}.'.format(nome))
elif nome in 'ANA CLÁUDIA JÉSSICA JULIANA':
    print('Belo nom feminino: {}'.format(nome))
else:
    print('{}, O seu nome normal!'.format(nome))
print('Tenha um Optimo dia, {}'.format(nome))