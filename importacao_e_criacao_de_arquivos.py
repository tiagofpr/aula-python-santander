#8. Importação e criação de módulos

"""
    Em Python, podemos organizar nosso código em módulos, que são arquivos contendo definições de funções, classes e variáveis. 
    Podemos importar esses módulos em outros arquivos para reutilizar o código.
    Para criar um módulo, basta criar um arquivo Python com a extensão .py e definir as funções, classes ou variáveis que desejamos incluir no módulo.
    Para importar um módulo, usamos a palavra-chave import seguida pelo nome do módulo. 
    Também podemos importar funções específicas de um módulo usando a sintaxe from <module> import <function>.
"""

#Importar módulos

import math  # Importando o módulo math, que fornece funções matemáticas

resultado = math.sqrt(16)  # Usando a função sqrt do módulo math para calcular a raiz quadrada
print(resultado)  # Saída: 4.0

from math import sqrt

resultado = sqrt(25)  # Usando a função sqrt diretamente, sem precisar do prefixo math.
print(resultado)  # Saída: 5.0

#Funções e classes de módulos padrão

"""
    O Python possui uma ampla biblioteca padrão que inclui módulos para diversas funcionalidades, como manipulação de arquivos, operações matemáticas, manipulação de datas e muito mais.
    Podemos explorar a documentação oficial do Python para conhecer os módulos disponíveis e suas funcionalidades.
"""

import random  # Importando o módulo random, que fornece funções para gerar números aleatórios
import datetime  # Importando o módulo datetime, que fornece classes para manipulação de datas e horários

numero_aleatorio = random.randint(1, 10)  # Gerando um número aleatório entre 1 e 10
print(numero_aleatorio)  # Saída: Um número aleatório entre 1 e 10

data_atual = datetime.datetime.now()  # Obtendo a data e hora atual
print(data_atual)  # Saída: A data e hora atual no formato YYYY-MM-DD HH:MM:SS.mmmmmm


#8.1. Criação de módulos próprios

"""
    Podemos criar nossos próprios módulos para organizar nosso código e torná-lo reutilizável. 
    Para isso, basta criar um arquivo Python com a extensão .py e definir as funções, classes ou variáveis que desejamos incluir no módulo.
    Em seguida, podemos importar esse módulo em outros arquivos para utilizar suas funcionalidades.
"""

#meu_modulo.py (criado em um arquivo separado)
# def saudar(nome):
#     return f"Olá, {nome}!"

# def calcular_soma(a, b):
#     return a + b

#Depois, podemos importar e utilizar as funções definidas em meu_modulo.py em outro arquivo Python.

import meu_modulo  # Importando o módulo meu_modulo

meu_modulo.saudar("João")  # Chamando a função saudar do módulo meu_modulo
resultado = meu_modulo.calcular_soma(5, 3)  # Chamando a função calcular_soma do módulo meu_modulo
print(resultado)  # Saída: 8

#Organização do código em módulos

"""
    Organizar o código em módulos é uma prática recomendada, pois facilita a manutenção, a legibilidade e a reutilização do código. 
    Podemos dividir nosso código em diferentes arquivos, cada um contendo funções ou classes relacionadas a uma funcionalidade específica.
    Além disso, podemos criar pacotes, que são diretórios contendo múltiplos módulos, para organizar ainda mais nosso código.
"""

#criado os arquivos operacoes.py e utilidades.py (em arquivos separados)
#operacoes.py
# def somar(a, b):
#    return a + b

#utilidades.py
# def imprimir_mensagem(mensagem):
#    print(mensagem)    

import operacoes  # Importando o módulo operacoes
import utilidades  # Importando o módulo utilidades

resultado =  operacoes.somar(10, 5)  # Chamando a função somar do módulo operacoes
utilidades.imprimir_mensagem(f"O resultado da soma é: {resultado}")  # Cham

nome = utilidades.obter_nome_usuario()  # Chamando a função obter_nome_usuario do módulo utilidades
utilidades.imprimir_mensagem(f"Olá, {nome}!")  # Chamando a função imprimir_mensagem do módulo utilidades
