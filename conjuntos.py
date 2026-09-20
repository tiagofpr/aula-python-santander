#4.3 Conjuntos (set)

"""
Um conjunto é um estrutura de dados mutável e  não ordenada quw permitte armazenar uma coleção de elementos unicos. Os conjuntos são delimitados
por chave {} ou  são criados utilizando a função set().
"""

#Criação e operações básicas
fruta = {"maçã", "banana", "laranja"}
numeros = set([1,2,3,4,5])

# os conjutos suportam operações matemáticas de conuntos, comoa a união (|), a interseção (&), a diferença (-) e a diferença simétrica (^). 
# Essas operações podem ser realizadas entre dois conjuntos, resultando em um novo conjunto.

conjunto1 ={1,2,3}
conjunto2 ={3,4,5}

uniao = conjunto1 | conjunto2
print(uniao)  # Saída: {1, 2, 3, 4, 5}

intersecao = conjunto1 & conjunto2
print(intersecao)  # Saída: {3}

diferenca = conjunto1 - conjunto2
print(diferenca) # imprime: {1, 2}

diferenca_simetrica = conjunto1 ^ conjunto2
print(diferenca_simetrica)  # Saída: {1, 2, 4, 5}

#métodos de conjuntos
"""
    add(elemento): Adiciona um elemento ao conjunto.
    remove(elemento): Remove um elemento do conjunto. Se o elemento não estiver presente, gera um erro.
    discard(elemento): Remove um elemento do conjunto, se estiver presente. Se o elemento não estiver presente, não gera erro.
    pop(): Remove e retorna um elemento aleatório do conjunto.
    clear(): Remove todos os elementos do conjunto, deixando-o vazio.
 """ 

frutas = {"maçã", "banana", "laranja"}

frutas.add("pera")  # Adiciona "pera" ao conjunto
print(frutas)  # Saída: {'maçã', 'banana', 'laranja', 'pera'}

frutas.remove("banana")  # Remove "banana" do conjunto
print(frutas)  # Saída: {'maçã', 'laranja', 'pera'}

frutas.discard("uva")  # Tenta remover "uva", mas não gera erro, pois não está presente
print(frutas)  # Saída: {'maçã', 'laranja', 'pera'}

frutas.clear()  # Remove todos os elementos do conjunto
print(frutas)  # Saída: set() (conjunto vazio)

