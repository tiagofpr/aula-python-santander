#PErgunta 1

#Qual valor terá a variavel de rsultado após executar o código a seguir em python?

# numero = 7
# se numero % 2 == 0:

# resultado = "Par"
# senão:
#     resultado = "Impar"

"""
    Esse código está com erros de sintaxe, pois em python precisamos deixar o código indentado.
    e também a palavra "senão" não é reconhecida, o correto seria "else".
"""

# O correto seria:
numero = 7
if numero %2 == 0:
    resultado = "Par"
else:
    resultado = "Impar"

print(resultado)


#pergunta 2

# Qual afirmação é veradeira sobre o código a seguir em python?

def multiplicar(a,b):
    return a*b

resultado = multiplicar(5,3) + multiplicar(2,4)

print(resultado)

"""
    A função multiplicar recebe dois argumentos a e b, e retorna o produto desses argumentos. 
    O resultado da expressão multiplicar(5,3) + multiplicar(2,4) será 15 + 8 = 23.
    Portanto, a afirmação verdadeira é que o código calcula a soma dos produtos de dois pares de números.
"""

#Pergunta 3

#Qual estrutura de dados em python é usada para armazenar uma coleção ordenadas e mutável de elementos.

"""
    A estrutura de dados em Python usada para armazenar uma coleção ordenada e mutável de elementos é a lista (list).
    As listas são definidas usando colchetes [] e os elementos são separados por vírgulas.
    Exemplo:
    frutas = ["maçã", "banana", "laranja"]
"""

