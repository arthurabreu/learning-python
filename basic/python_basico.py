# Basicao
print("Hello World!")
print(f'1+2 = {1+2}')
print(f'1-2 = {1-2}')
print(f'4*5 = {4*5}')
print(f'10/4 = {10/4}')
print(f'5**2 = {5**2}')
print(f'2 * 4 + 6 = {2 * 4 + 6}')
print(f'2 * (4 + 6) = {2 * (4 + 6)}')
print('Meu nome é Arthur')
print('Cruzeiro ' * 3)
print(f'Concatenacao basica de strings 30 + ___ + ??? = {'30' + '___' + '???'}')
print(f'The length of Arthur is {len("Arthur")}')
print(f'O tipo do numeral 5 é: {type(5)}')
print('-' * 15)
# Variaveis
pi = 3.14
raio = 5
raio_ao_quadrado = raio ** 2
print(f'A area do circulo é {pi * raio_ao_quadrado}')
print('-' * 15)
# Pegando valores do Usuario
nome = input('Qual é o seu nome? ')
print(f'Olá {nome}!')
x = input('Digite um número: ')
x_num = float(x)
print(f'Seu numero + 10: {x_num + 10}')
print('-' * 15)
# Desafio - Crie um programa que: 
# - Pergunte o nome do usuário e a idade do usuário
# - Da oi pra voce
# - Conta quantas letras seu nome possui
# - Fala quantos anos voce tera daqui cinco anos
print('Por favor, responda as perguntas abaixo:')
nome = input('Qual é o seu nome? ')
idade = input('Qual é a sua idade? ')
print(f'Olá {nome}!')
print(f'Seu nome possui {len(nome)} letras.')
print(f'Daqui cinco anos você terá {int(idade) + 5} anos.')
print('-' * 15)