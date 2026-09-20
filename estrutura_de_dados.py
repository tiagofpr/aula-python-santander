# 4 Estrutura de Dados

#Listas
# Uma lista é uma coleção ordenada e mutável de elementos, que podem ser de diferentes tipos de dados. As listas são definidas usando colchetes [] e os elementos são separados por vírgulas.

#criando uma lista
frutas = ["maçã", "banana", "laranja"]
print(frutas)  # Saída: ['maçã', 'banana', 'laranja']
print(frutas[0])  # Saída: 'maçã' (acessando o primeiro elemento da lista)
print(frutas[1])  # Saída: 'banana' (acessando o segundo elemento da lista)
print(frutas[2])  # Saída: 'laranja' (acessando o terceiro elemento da lista)

print(frutas[-1])  # Saída: 'laranja' (acessando o último elemento da lista)
print(frutas[-2])  # Saída: 'banana' (acessando o penúltimo elemento da lista)
print(frutas[-3])  # Saída: 'maçã' (acessando o antepenúltimo elemento da lista)

#métodos de listas
"""
    append(elemento): Adiciona um elemento ao final da lista.
    insert(indice, elemento): Insere um elemento em uma posição específica da lista.
    remove(elemento): Remove a primeira ocorrência de um elemento da lista.
    pop(indice): Remove e retorna o elemento em uma posição específica da lista (ou o último elemento, se nenhum índice for fornecido).
    sort(): Ordena os elementos da lista em ordem crescente.
    reverse(): Inverte a ordem dos elementos da lista.
    len(): Retorna o número de elementos na lista.
"""

#exemplo de uso dos métodos de listas
frutas.append("uva")  # Adiciona "uva" ao final da lista
print(frutas)  # Saída: ['maçã', 'banana', 'laranja', 'uva']   

frutas.insert(1, "morango")  # Insere "morango" na posição 1 da lista
print(frutas)  # Saída: ['maçã', 'morango', 'banana', 'laranja', 'uva']   

frutas.remove("banana")  # Remove a primeira ocorrência de "banana" da lista
print(frutas)  # Saída: ['maçã', 'morango', 'laranja', 'uva']   

fruta_removida = frutas.pop(0)  # Remove e retorna o elemento na posição 0 da lista
print(fruta_removida)  # Saída: 'maçã'
print(frutas)  # Saída: ['morango', 'laranja', 'uva']   

frutas.sort()  # Ordena os elementos da lista em ordem crescente
print(frutas)  # Saída: ['laranja', 'morango', 'uva']   

frutas.reverse()  # Inverte a ordem dos elementos da lista
print(frutas)  # Saída: ['uva', 'morango', 'laranja']   

numero_de_elementos = len(frutas)  # Retorna o número de elementos na lista
print(numero_de_elementos)  # Saída: 3  

#Lista de compreensão
# Uma lista de compreensão é uma maneira concisa de criar listas em Python. Ela permite criar uma nova lista aplicando uma expressão a cada elemento de uma sequência ou iterável, opcionalmente filtrando os elementos com base em uma condição.   
#nova_lista = [expressao for elemento in sequencia if condicao]

numeros = [1, 2, 3, 4, 5]
# Criando uma nova lista com os quadrados dos números da lista original
quadrados = [numero ** 2 for numero in numeros if numero % 2 == 0]
print(quadrados)  # Saída: [4, 16]