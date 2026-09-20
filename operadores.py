#2.2 Operadores
"""
Operadores são símbolos que realizam operações em valores ou variáveis.
    Soma (+): soma dois valores.
    Subtração (-): subtrai o segundo valor do primeiro.
    Multiplicação (*): multiplica dois valores.
    Divisão (/): divide o primeiro valor pelo segundo e devolve um resultado de tipo flutuante.
    Divisão inteira (//): divide o primeiro valor pelo segundo e devolve um resultado de tipo inteiro (a parte decimal é descartada).
    Módulo (%): devolve o resto da divisão entre o primeiro valor e o segundo.
    Exponenciação (**): eleva o primeiro valor à potência do segundo.   
"""

a = 10
b = 3

soma = a + b  # Soma: 10 + 3 = 13
subtracao = a - b  # Subtração: 10 - 3 = 7
multiplicacao = a * b  # Multiplicação: 10 * 3 = 30
divisao = a / b  # Divisão: 10 / 3 = 3.3333333333333335
divisao_inteira = a // b  # Divisão inteira: 10 // 3 = 3
modulo = a % b  # Módulo: 10 % 3 = 1
exponenciacao = a ** b  # Exponenciação: 10 ** 3 = 1000

# OPeradores de comparação
"""
OS operadores de comparação são usados para comparar valores e retornam um valor booleano (True ou False).
    Igual a (==): verifica se dois valores são iguais.
    Diferente de (!=): verifica se dois valores são diferentes.
    Maior que (>): verifica se o primeiro valor é maior que o segundo.
    Menor que (<): verifica se o primeiro valor é menor que o segundo.
    Maior ou igual a (>=): verifica se o primeiro valor é maior ou igual ao segundo.
    Menor ou igual a (<=): verifica se o primeiro valor é menor ou igual ao segundo.
"""

a = 10
b = 5

igual = a == b  # Igual a: 10 == 5 -> False
diferente = a != b  # Diferente de: 10 != 5 -> True
maior = a > b  # Maior que: 10 > 5 -> True
menor = a < b  # Menor que: 10 < 5 -> True
maior_ou_igual = a >= b  # Maior ou igual a:    10 >= 5 -> True
menor_ou_igual = a <= b  # Menor ou igual a: 10 <= 5 -> False

# OPeradores lógicos
"""
OS operadores lógicos são usados para combinar expressões booleanas e retornam um valor booleano (True ou False).
    E (and): retorna True se ambas as expressões forem verdadeiras.
    OU (or): retorna True se pelo menos uma das expressões for verdadeira.
    NÃO (not): inverte o valor booleano da expressão.
"""                                                                                 

a = 10
b = 3

resultado_and =(a > 5) and (a < 5) #True
resultado_or = (a > 5) or (a < 5) #True
resultado_not = not (a > 5) #False

#Voce pode usar operadores lógicos para combinar várias condições em uma única expressão. 
# Por exemplo, você pode verificar se um número está dentro de um intervalo usando o operador "and":


