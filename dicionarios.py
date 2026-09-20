#4.2 Dicionarios

# um dicionario é um estrutura de dados mutável e não ordenda que permite armazenar pares de chave-valor. Cada elemento em um dicionario consiste em uma 
#chave única e seu valor correspondente. Os dicionarios são delimitados por chaves {}, e os parec chave-valor são separados por virgulas.

# Criação e acesso

pessoa = {"nome": "jõao", "idade": 25, "cidade":"Madri"}
print(pessoa["nome"]) # Imprime "jõao"
print(pessoa["idade"]) # Imprime 25
print(pessoa["cidade"]) # Imprime "Madri"

#podemos usar o metodo get() para acessar os valores de um dicionario. O metodo get() retorna o valor associado a uma chave especifica, e se a chave não existir, ele retorna None ou um valor padrao especificado.
print(pessoa.get("nome")) # Imprime "jõao"
print(pessoa.get("idade")) # Imprime 25
print(pessoa.get("cidade")) # Imprime "Madri"

# Métodos de dicionarios
"""
    keys(): Retorna uma lista contendo todas as chaves do dicionario.
    values(): Retorna uma lista contendo todos os valores do dicionario.
    items(): Retorna uma lista de tuplas, onde cada tupla contém um par chave-valor do dicionario.
    update(outro_dicionario): Atualiza o dicionario com os pares chave-valor de outro dicionario.
    pop(chave): Remove o par chave-valor correspondente a uma chave especifica e retorna o valor removido.
    clear(): Remove todos os pares chave-valor do dicionario, deixando-o vazio.
"""

print("Exemplo de keys():")
pessoa = {"nome": "jõao", "idade": 25, "cidade":"Madri"}
chaves = pessoa.keys()
print(chaves)  # Saída: dict_keys(['nome', 'idade', 'cidade'])
print("\nExemplo de values():")
valores = pessoa.values()
print(valores)  # Saída: dict_values(['jõao', 25, 'Madri'])
print("\nExemplo de items():")
pares = pessoa.items()
print(pares)  # Saída: dict_items([('nome', 'jõao'), ('idade', 25), ('cidade', 'Madri')])
print("\nExemplo de update():")
outro_dicionario = {"profissao": "engenheiro", "salario": 5000}
pessoa.update(outro_dicionario)
print(pessoa)  # Saída: {'nome': 'jõao', 'idade': 25, 'cidade': 'Madri', 'profissao': 'engenheiro', 'salario': 5000}
print("\nExemplo de pop():")
idade_removida = pessoa.pop("idade")
print(idade_removida)  # Saída: 25
print(pessoa)  # Saída: {'nome': 'jõao', 'cidade': 'Madri', 'profissao': 'engenheiro', 'salario': 5000}
print("\nExemplo de clear():")
pessoa.clear()
print(pessoa)  # Saída: {} 
