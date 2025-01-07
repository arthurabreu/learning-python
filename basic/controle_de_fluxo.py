# Controle de fluxo
########## - if, elif, else - Estruturas de controle de fluxo condicional ##########
print('-' * 20)
print('Controle de fluxo')
print('-' * 20)
print('-' * 15 + 'if, elif, else' + '-' * 15)
idade = int(input('Qual é a sua idade? '))
if idade < 18:
    print('Você é menor de idade.')
elif idade == 18:
    print('Você tem 18 anos.')
else:
    print('Você é maior de idade.')


########## - while - Loop que continua enquanto a condição for verdadeira ##########
print('-' * 15 + 'while - Loop que continua enquanto a condição for verdadeira' + '-' * 15)
x = 0
while x < 10:
    print(x)
    x += 1


########## - for - Loop que itera sobre uma sequência ##########
print('-' * 15 + 'for - Loop que itera sobre uma sequência' + '-' * 15)
for i in range(10):
    print(i)

valores = [1, 2, 3, 4, 5]
for valor in valores:
    print(valor)
    
clientes = [('João', '90439230432', 'joao@gmail.com'), ('Maria', '023940234', 'maria@gmail.com'), ('José', '0239402394', 'jose@gmail.com')]
for nome, cpf, email in clientes:
    print(nome, cpf, email)
    
for cliente in clientes:
    nome = cliente[0]
    cpf = cliente[1]
    email = cliente[2]
    print(nome, cpf, email)


########## - range - Gera uma sequência de números ##########
print('-' * 15 + 'range - Gera uma sequência de números' + '-' * 15)
for i in range(5, 10):
    print(i)
    
print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(5, 10))) # [5, 6, 7, 8, 9]
print(list(range(0, 10, 2))) # [0, 2, 4, 6, 8]
print(list(range(10, 0, -1))) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# range(10, 0, -1):
#Início: 10
#Fim: 0 (não incluso)
#Passo: -1
#Isso cria uma sequência de números começando em 10 e diminuindo de 1 em 1 até chegar a 1.
    
########## - break - Interrompe o loop ##########
print('-' * 15 + 'break - Interrompe o loop' + '-' * 15)
for i in range(10):
    if i == 5:
        break
    print(i)


########## - continue - Pula para a próxima iteração do loop ##########
print('-' * 15 + 'continue - Pula para a próxima iteração do loop' + '-' * 15)
for i in range(10):
    if i == 5:
        continue
    print(i)


########## - pass - Não faz nada, usado como placeholder ##########
print('-' * 15 + 'pass - Não faz nada, usado como placeholder' + '-' * 15)
for i in range(10):
    if i == 5:
        pass
    print(i)


########## - try, except - Tratamento de exceções ##########
print('-' * 15 + 'try, except - Tratamento de exceções' + '-' * 15)
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print('Erro: divisão por zero.')
except Exception as e:
    print(f'Erro: {e}')
finally:
    print('Bloco finally executado.')


########## - funções, def - Define uma função que pode ser chamada posteriormente ##########
print('-' * 15 + 'funções - Define uma função que pode ser chamada posteriormente' + '-' * 15)
def soma(a, b):
    return a + b

resultado = soma(5, 3)
print(f'O resultado da soma é {resultado}')

def adicionar_final(text, final='!'):
    return text + final	
print(adicionar_final('Olá'))  # Olá!

#None - null em Python
def funcao():
    pass
print(funcao())  # None




########## - listas - Estrutura de dados que armazena uma sequência de elementos, que podem ser modificados ##########
print('-' * 15 + 'listas - Estrutura de dados que armazena uma sequência de elementos' + '-' * 15)
lista = [1, 2, 3, 4, 5]
for item in lista:
    print(item)
    
# Criação de um dicionário
dicionario = {
    'nome': 'João',
    'idade': 30,
    'cidade': 'São Paulo'
}

########## - get() - Retorna o valor de uma chave, com opção de valor padrão ##########
valor = dicionario.get('nome')  # Retorna 'João'
valor_inexistente = dicionario.get('pais', 'Brasil')  # Retorna 'Brasil'
print(valor)
print(valor_inexistente)

########## - update() - Atualiza o dicionário com pares chave-valor de outro dicionário ##########
dicionario_update = {'idade': 31, 'profissao': 'Engenheiro'}
dicionario.update(dicionario_update)
print(dicionario)

########## - items() - Retorna uma lista de tuplas (chave, valor) ##########
itens = dicionario.items()
print(itens)

########## - keys() - Retorna uma lista das chaves do dicionário ## ########
chaves = dicionario.keys()
print(chaves)

########## - values() - Retorna uma lista dos valores do dicionário ##########
valores = dicionario.values()
print(valores)

########## - pop() - Remove e retorna o valor de uma chave específica ##########
idade = dicionario.pop('idade')
print(f"Idade removida: {idade}")
print(dicionario)

########## - popitem() - Remove e retorna o último par chave-valor adicionado ##########
ultimo_item = dicionario.popitem()
print(f"Último item removido: {ultimo_item}")
print(dicionario)

########## - clear() - Remove todos os itens do dicionário ##########
dicionario.clear()
print(dicionario)    
    
#Compreensao de listas    
valores = list (range (10))
maiores_que_cinco = []
for val in valores:
    if val > 5:
        maiores_que_cinco.append(val) 
# mesma coisa do codigo acima, com apenas uma linha
maiores_que_cinco_2 = [valor for valor in valores if valor > 5]  
# resultado esperado [valor]
# pra cada um dos elementos de uma sequencia que estou passando [for valor in valores]
# se o valor for maior que 5 [if valor > 5]
# Estrutura mais limpa:
maiores_que_cinco_3 = [
    resultado 
    for resultado in valores
    if resultado > 5
]  
print(maiores_que_cinco_3) # [6, 7, 8, 9]




    
########## - tuplas - Estrutura de dados que armazena uma sequência de elementos, que nao podem ser modificados ##########   
print('-' * 15 + 'tuplas - Estrutura de dados que armazena uma sequência de elementos' + '-' * 15)
tupla = (1, 2, 3, 4, 5)
for item in tupla:
    print(item)
    
    
    
    
########## - sequencias -  ########## 
print('-' * 15 + 'sequencias - ' + '-' * 15)
nome = 'Arthur'
list(nome)
print(list(nome))   




########## - slicing -  ########## 
print('-' * 15 + 'slicing - ' + '-' * 15)
pessoas = ['Arthur', 'João', 'Maria', 'José'] # 0,1,2,3
print(pessoas[1:3]) # ['João', 'Maria'], para antes do terceiro elemento. 1:3 podemos pensar em 3-1, ou seja, 2 elementos sao retornados
print(pessoas[:2]) # ['Arthur', 'João']

nome = 'Arthur'
print(nome[1:3]) # 'rt'
print(nome[:3]) # 'Art'
print(nome[3:]) # 'hur'
print(nome[:]) # 'Arthur'

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numeros[0:len(numeros):2] # [1, 3, 5, 7, 9]
numeros[::2] # [1, 3, 5, 7, 9]
numeros[::-1] # [9, 8, 7, 6, 5, 4, 3, 2, 1]
numeros[::-2] # [9, 7, 5, 3, 1]




########## - dicionários - Estrutura de dados que armazena pares chave-valor ##########
print('-' * 15 + 'dicionários - Estrutura de dados que armazena pares chave-valor' + '-' * 15)
dicionario = {'nome': 'João', 'idade': 30}
for chave, valor in dicionario.items():
    print(f'{chave}: {valor}')
    
# Criação de um dicionário
dicionario = {
    'nome': 'João',
    'idade': 30,
    'cidade': 'São Paulo'
}

########## - get() - Retorna o valor de uma chave, com opção de valor padrão ##########
valor = dicionario.get('nome')  # Retorna 'João'
valor_inexistente = dicionario.get('pais', 'Brasil')  # Retorna 'Brasil'
print(valor)
print(valor_inexistente)

########## - update() - Atualiza o dicionário com pares chave-valor de outro dicionário ##########
dicionario_update = {'idade': 31, 'profissao': 'Engenheiro'}
dicionario.update(dicionario_update)
print(dicionario)

########## - items() - Retorna uma lista de tuplas (chave, valor) ##########
itens = dicionario.items()
print(itens)

########## - keys() - Retorna uma lista das chaves do dicionário ##########
chaves = dicionario.keys()
print(chaves)

########## - values() - Retorna uma lista dos valores do dicionário ##########
valores = dicionario.values()
print(valores)

########## - pop() - Remove e retorna o valor de uma chave específica ##########
idade = dicionario.pop('idade')
print(f"Idade removida: {idade}")
print(dicionario)

########## - popitem() - Remove e retorna o último par chave-valor adicionado ##########
ultimo_item = dicionario.popitem()
print(f"Último item removido: {ultimo_item}")
print(dicionario)

########## - clear() - Remove todos os itens do dicionário ##########
dicionario.clear()
print(dicionario)    





########## - lambda - Função anônima que pode ter qualquer número de argumentos, mas apenas uma expressão ##########
print('-' * 15 + 'lambda - Função anônima que pode ter qualquer número de argumentos, mas apenas uma expressão' + '-' * 15)
soma = lambda a, b: a + b
print(soma(5, 3))




########## - map - Aplica uma função a todos os itens de uma lista ##########
print('-' * 15 + 'map - Aplica uma função a todos os itens de uma lista' + '-' * 15)
lista = [1, 2, 3, 4, 5]
nova_lista = list(map(lambda x: x * 2, lista))
print(nova_lista)




########## - filter - Filtra itens de uma lista que satisfazem uma condição ##########
print('-' * 15 + 'filter - Filtra itens de uma lista que satisfazem uma condição' + '-' * 15)
lista = [1, 2, 3, 4, 5]
nova_lista = list(filter(lambda x: x % 2 == 0, lista))
print(nova_lista)




########## - reduce - Aplica uma função cumulativa aos itens de uma lista ##########
print('-' * 15 + 'reduce - Aplica uma função cumulativa aos itens de uma lista' + '-' * 15)
from functools import reduce
lista = [1, 2, 3, 4, 5]
resultado = reduce(lambda x, y: x + y, lista)
print(resultado)




########## - global - Declara uma variável global dentro de uma função ##########
# Em Python, a palavra-chave global é usada para declarar que uma variável dentro de uma função é global, 
# ou seja, ela não é local à função, mas sim uma variável que existe no escopo global (fora de todas as funções). 
# Explicação Passo a Passo:
# Declaração Global: x = 0
# Aqui, x é uma variável global inicializada com o valor 0.
# Definição da Função: def f():
# Define uma função f.
# Uso da Palavra-chave global: global x
# Dentro da função f, a palavra-chave global é usada para indicar que x refere-se à variável global x declarada fora da função.
# Sem essa declaração, x seria tratado como uma variável local à função f.
# Modificação da Variável Global: x = 1
# Atribui o valor 1 à variável global x.
# Chamada da Função: f()
# Chama a função f, que modifica o valor de x para 1.
# Impressão do Valor de x: print(x)
# Imprime o valor de x, que agora é 1, pois a função f modificou a variável global x.
print('-' * 15 + 'global - Declara uma variável global dentro de uma função' + '-' * 15)
# Explicação Passo a Passo:
# Declaração Global: x = 0
# Aqui, x é uma variável global inicializada com o valor 0.
x = 0

# Definição da Função: def f()
# Define uma função f.
def f():
    # Uso da Palavra-chave global: global x
    # Dentro da função f, a palavra-chave global é usada para indicar que x refere-se à variável global x declarada fora da função.
    # Sem essa declaração, x seria tratado como uma variável local à função f.
    global x
    # Modificação da Variável Global: x = 1
    # Atribui o valor 1 à variável global x.
    x = 1

# Chamada da Função: f()
# Chama a função f, que modifica o valor de x para 1.
f()

# Impressão do Valor de x: print(x)
# Imprime o valor de x, que agora é 1, pois a função f modificou a variável global x.
print(x)





########## - nonlocal - Declara uma variável não local dentro de uma função aninhada ##########
print('-' * 15 + 'nonlocal' + '-' * 15)
def f():
    x = 0
    def g():
        nonlocal x
        x = 2
    g()
    print(x)
f()





########## - return - Retorna um valor de uma função ##########
print('-' * 15 + 'return' + '-' * 15)
def f():
    return 1
print(f())





########## - yield - Produz uma sequência de valores de uma função geradora ##########
print('-' * 15 + 'yield' + '-' * 15)
def f():
    yield 1
    yield 2
for i in f():
    print(i)





########## - class - Define uma classe ##########
print('-' * 15 + 'class' + '-' * 15)
class A:
    pass
print(A)





########## - def - Define uma função ##########
print('-' * 15 + 'def' + '-' * 15)
def f():
    pass
print(f)





########## - exec - Executa uma string de código Python ##########
print('-' * 15 + 'exec' + '-' * 15)
code = """
def greet(name):
    return f'Hello, {name}!'
print(greet('Arthur'))
"""
exec(code)  # Executa a string de código Python que define e chama a função greet





########## - locals - Retorna um dicionário das variáveis locais atuais ##########
print('-' * 15 + 'locals' + '-' * 15)
def example_locals():
    a = 10
    b = 20
    print(locals())  # Imprime um dicionário das variáveis locais atuais
example_locals()





########## - vars - Retorna um dicionário das variáveis locais e globais atuais ##########
print('-' * 15 + 'vars' + '-' * 15)
class Example:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show_vars(self):
        print(vars(self))  # Imprime um dicionário das variáveis de instância (atributos) do objeto

example = Example(5, 10)
example.show_vars()





########## - dir - Retorna uma lista dos nomes no escopo local atual ##########
print('-' * 15 + 'dir' + '-' * 15)
class ExampleDir:
    def __init__(self):
        self.a = 1
        self.b = 2

example_dir = ExampleDir()
print(dir(example_dir))  # Imprime uma lista dos nomes dos atributos do objeto example_dir





########## - finally - Bloco que sempre será executado, independentemente de uma exceção ter sido lançada ou não ##########
print('-' * 15 + 'finally' + '-' * 15)
try:
    x = 1 / 0
except ZeroDivisionError:
    print('Erro: Divisão por zero.')
finally:
    print('Fim do bloco try.')





########## - raise - Lança uma exceção ##########
print('-' * 15 + 'raise' + '-' * 15)
try:
    raise ValueError('Erro customizado.')
except ValueError as e:
    print(e)





########## - with - Gerencia contextos de recursos (como arquivos) ##########
print('-' * 15 + 'with' + '-' * 15)
with open('arquivo.txt', 'w') as f:
    f.write('Hello World!')
    print('Arquivo aberto.')
with open('arquivo.txt', 'r') as f:
    content = f.read()
    print('Conteúdo do arquivo:', content)
print('Arquivo fechado.')





########## - as - Atribui um nome a uma exceção capturada ##########
print('-' * 15 + 'as' + '-' * 15)
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(e)





########## - in - Verifica se um valor está contido em uma sequência ##########
print('-' * 15 + 'in' + '-' * 15)
print('a' in 'banana')





########## - is - Verifica se dois objetos são o mesmo objeto ##########
print('-' * 15 + 'is' + '-' * 15)
print(1 is 1)





########## - and - Operador lógico AND ##########
print('-' * 15 + 'and' + '-' * 15)
print(1 == 1 and 2 == 2)





########## - or - Operador lógico OR ##########
print('-' * 15 + 'or' + '-' * 15)
print(1 == 1 or 2 == 3)





########## - not - Operador lógico NOT ##########
print('-' * 15 + 'not' + '-' * 15)
print(not 1 is 1)





########## - assert - Verifica uma condição e lança uma exceção se a condição for falsa ##########
print('-' * 15 + 'assert' + '-' * 15)
assert 1 == 1





########## - del - Deleta uma variável ##########
print('-' * 15 + 'del' + '-' * 15)
x = 1
del x
try:
    print(x)
except NameError:
    print('Variável não definida.')

    
    
    
    
########## - from - Importa um nome específico de um módulo ##########
print('-' * 15 + 'from' + '-' * 15)
from math import pi
print(pi)
    
    




########## - import - Importa um módulo ##########
print('-' * 15 + 'import' + '-' * 15)
import math
print(math.pi)
        
        
    
        
#Dado uma sequência de números, calcule a soma e média dos números.
#ATENÇÃO: não vale usar a função sum() !
#Dado uma sequência de números, calcule o maior valor da sequência.
#ATENÇÃO: não vale usar a função max() !
#Dado uma lista de palavras, printe todas as palavras com pelo menos 5 caracteres. 

# 1. Calcular soma e média sem usar sum()
def calcular_soma_media(numeros):
    soma = 0
    for numero in numeros:
        soma += numero
    media = soma / len(numeros) if numeros else 0
    return soma, media

# 2. Calcular o maior valor sem usar max()
def encontrar_maior(numeros):
    if not numeros:
        return None
    maior = numeros[0]
    for numero in numeros:
        if numero > maior:
            maior = numero
    return maior

# 3. Imprimir palavras com pelo menos 5 caracteres
def imprimir_palavras_longas(palavras):
    for palavra in palavras:
        if len(palavra) >= 5:
            print(palavra)

# Exemplos de uso
if __name__ == "__main__":
    numeros = [10, 20, 30, 40, 50]
    palavras = ["casa", "telefone", "carro", "bicicleta", "sol"]

    soma, media = calcular_soma_media(numeros)
    print(f"Soma: {soma}, Média: {media}")

    maior = encontrar_maior(numeros)
    print(f"Maior número: {maior}")

    print("Palavras com pelo menos 5 caracteres:")
    imprimir_palavras_longas(palavras)
    
    
# IMPORTS COMUNS    
# import math # Módulo de funções matemáticas
# import datetime # Módulo de funções de data e hora
# import random # Módulo de funções de geração de números aleatórios
# import os # Módulo de funções do sistema operacional
# import sys # Módulo de funções e variáveis do Python
# import json # Módulo de funções de manipulação de JSON
# import csv # Módulo de funções de manipulação de CSV
# import re # Módulo de funções de expressões regulares
# import requests # Módulo de funções de requisições HTTP
# import sqlite3 # Módulo de funções de banco de dados SQLite
# import pandas # Módulo de funções de manipulação de dados tabulares
# import numpy # Módulo de funções de manipulação de arrays e matrizes
# import matplotlib.pyplot as plt # Módulo de funções de visualização de dados
# import seaborn # Módulo de funções de visualização de dados
# import tensorflow # Módulo de funções de aprendizado de máquina
# import torch # Módulo de funções de aprendizado de máquina
# import sklearn # Módulo de funções de aprendizado de máquina
# import keras # Módulo de funções de aprendizado de máquina
# import nltk # Módulo de funções de processamento de linguagem natural
# import spacy # Módulo de funções de processamento de linguagem natural
# import gensim # Módulo de funções de processamento de linguagem natural
# import textblob # Módulo de funções de processamento de linguagem natural
# import scrapy # Módulo de funções de web scraping
# import selenium # Módulo de funções de web scraping
# import bs4 # Módulo de funções de web scraping
# import flask # Módulo de funções de desenvolvimento web
# import django # Módulo de funções de desenvolvimento web
# import fastapi # Módulo de funções de desenvolvimento web
# import streamlit # Módulo de funções de desenvolvimento web
# import pytest # Módulo de funções de testes
# import unittest # Módulo de funções de testes
# import logging # Módulo de funções de logging
# import time # Módulo de funções de tempo
# import threading # Módulo de funções de programação concorrente
# import multiprocessing # Módulo de funções de programação concorrente
# import concurrent.futures # Módulo de funções de programação concorrente
# import asyncio # Módulo de funções de programação assíncrona
# import aiohttp # Módulo de funções de programação assíncrona
# import telebot # Módulo de funções de bots de Telegram
# import discord # Módulo de funções de bots de Discord