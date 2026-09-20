#4.1 Tuplas

#Uma tupla é uma estrutura de dados imutável e ordenada que permite armazenar uma coleção de elementos. Os elementos de uma tupla são encerrados entre parênteses () e separados por vírgulas. 
# Diferentemente das listas, as tuplas não podem ser modificadas após a sua criação, ou seja, não é possível adicionar, remover ou alterar elementos de uma tupla.

# Criação e acesso.

#Para ciar uma tupla, encerre os elementos entre parênteses () e separe-os por vírgulas.
#Exemplo:
ponto =(3,4)
print(ponto[0]) # Imprime 3
print(ponto[1]) # Imprime 4

#Ao contrário das listas, as tuplas são imutáveis, o que significa que você não pode adicionar, remover ou alterar elementos de uma tupla após a sua criação. No entanto, você pode criar uma nova tupla com os elementos desejados.

#Métodos de tuplas
#As tuplas possuem alguns métodos úteis, como count() e index().
#O método count() retorna o número de ocorrências de um elemento em uma tupla.
#Exemplo:
print('Exemplo de metodo count(), index() e len() em tuplas:')
print("Exemplo de count():")
tupla = (1, 2, 3, 2, 4, 2)
ocorrencias = tupla.count(2)
print(ocorrencias)  # Saída: 3
#O método index() retorna o índice da primeira ocorrência de um elemento em uma tupla.
#Exemplo:
print("Exemplo de index():")
tupla = (1, 2, 3, 4, 5)
indice = tupla.index(3)
print(indice)  # Saída: 2   
#O metodo len() retorna o número de elementos em uma tupla.
#Exemplo:
print("Exemplo de len():")
tupla = (1, 2, 3, 4, 5)
tamanho = len(tupla)
print(tamanho)  # Saída: 5  