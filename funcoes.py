# 5. Funções

"""
    As funções são blocos de códigos reutilizaveis que nos permite encapsular tarefas específicas e executa-las quando necessário.
    AS funções nos ajudam a orgainizar o código, tornando-o mais legível e modular.
    Em Python, podemos definir uma função usando a palavra-chave "def", seguida pelo nome da função, parênteses e dois pontos. O corpo da função é indentado e pode conter instruções que serão executadas quando a função for chamada.
    Podemos passar argumentos para a função, que são valores que a função pode usar para realizar suas operações. Além disso, uma função pode retornar um valor usando a palavra-chave "return".
"""

# Definição  e chamada de uma função.

def saudacao():
    print("Olá! Bem-vindo(a) ao nosso programa.")

saudacao()  # Chamada da função

#Paramtros e argumentos
def saudacao_com_argumento(nome):
    print(f"olá, {nome}!")

saudacao_com_argumento("João")  # Chamada da função com argumento
saudacao_com_argumento("Maria")  # Chamada da função com argumento

#Valores de retorno
def soma(a,b):
    return a + b

resultado = soma(5,3)
print(resultado)  # Saída: 8

#Funções anonimas (lambda)
"""
Python permite criar funçoes anomimas ou funções lambda, que são funções sem nome definidas em uma uínca linha. 
São comummente usadas quando precisamos de uma função simples e rápida,sem a necessidade de defini-la formalmente.
"""
quadrado = lambda x: x ** 2
print(quadrado(5))  # Saída: 25

#Escopo das variáveis (local vs. global)

"""
    O escopo das variáveis em Python determina onde uma variável pode ser acessada dentro do código. 
    Variáveis definidas dentro de uma função têm escopo local, o que significa que só podem ser acessadas dentro dessa função. 
    Variáveis definidas fora de qualquer função têm escopo global, podendo ser acessadas em qualquer parte do código.
"""
def funcao():
    variavel_local = 10
    print(variavel_local)  # Acessando a variável local dentro da função

variavel_global = 20

def funcao2():
    print(variavel_global)  # Acessando a variável global de qualquer lugar

funcao()  # Saída: 10
funcao2()  # Saída: 20  
print(variavel_global)  # Saída: 20
##print(variavel_local)  # Isso gerará um erro, pois variavel_local não está definida no escopo global

##Funções definidas pelo usuário

"""
    Em Python, podemos definir nossas próprias funções para realizar tarefas específicas. 
    Isso nos permite criar código modular e reutilizável, facilitando a manutenção e a legibilidade do programa.
    Para definir uma função, usamos a palavra-chave "def", seguida pelo nome da função, parênteses e dois pontos. 
    O corpo da função é indentado e pode conter instruções que serão executadas quando a função for chamada.
"""

def calcular(*numeros):
    soma = sum(numeros)
    quantidade = len(numeros)
    media = soma / quantidade
    return media

print("Media:", calcular(10, 20, 30, 40))  # Saída: Média: 25.0

def somar_3(x):
    return x + 3

somar = lambda x: x + 3

print("Soma com função definida pelo usuário:", somar_3(5))  # Saída: 8

#Documentação de funções

"""
    A documentação de funções em Python é feita usando docstrings, que são strings de documentação colocadas logo após a definição da função. 
    Elas fornecem informações sobre o propósito da função, seus parâmetros e o valor de retorno. 
    As docstrings são acessíveis em tempo de execução e podem ser visualizadas usando a função help().
"""

def area_retangulo(base, altura):
    """
    Calcula a área de um retângulo.

    Parâmetros:
    base (float): A base do retângulo.
    altura (float): A altura do retângulo.

    Retorna:
    float: A área do retângulo.
    """
    return base * altura

#Funções com numeros de variavel de argumentos
def soma_variacel(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print("Soma de vários números:", soma_variacel(1, 2, 3, 4, 5))  # Saída: 15
print("Soma de outros números:", soma_variacel(10, 20, 30))  # Saída: 60