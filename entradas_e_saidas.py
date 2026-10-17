# 7 Entradas e Saídas
"""
    Em Python, podemos interagir com o usuário por meio de entradas e saídas. 
    A função input() é usada para receber dados do usuário, enquanto a função print() é usada para exibir informações na tela.
    Podemos formatar a saída usando f-strings ou o método format() para tornar as mensagens mais legíveis e informativas.
"""

#Entrada de dados
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

print(f"Olá, {nome}! Você tem {idade} anos.")
print("Você tem " + idade + " anos.")  # Outra forma de concatenar strings

"""
Importante: A função input() sempre retorna uma string, então se você precisar de um número, será necessário converter a entrada usando int() ou float().
"""

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")


#Saída de dados
"""
    A função print() é usada para exibir informações na tela. 
    Podemos passar múltiplos argumentos para a função print(), separados por vírgulas, e ela irá concatená-los com um espaço entre eles.
    Além disso, podemos usar o parâmetro end para controlar o que é exibido no final da linha (por padrão, é uma nova linha).
"""

nome = "Tiago"
print("Olá,", nome)  
idade = 35

print("Idade:", idade, end=" anos\n")  # Usando o parâmetro end para adicionar " anos" no final da linha

#7.1 Leitura e escrita de arquivos
"""
    Em Python, podemos ler e escrever arquivos usando a função open().
    Para ler um arquivo, usamos o modo "r" (read), e para escrever em um arquivo, usamos o modo "w" (write) ou "a" (append).
    É importante sempre fechar o arquivo após a leitura ou escrita, usando o método close(), para liberar os recursos do sistema.
    Também podemos usar o gerenciador de contexto with, que garante que o arquivo seja fechado automaticamente após o bloco de código ser executado.
"""

#Leitura de arquivos
"""
    Para ler o conteúdo de um arquivo, primeiro devemos abri-lo utilizando a função open() em modo de leitura ("r"). Depois, podemos ler o conteúdo do arquivo utilizando métodos como read() ou readlines().
"""
arquivo = open("exemplo.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()  # Fechando o arquivo após a leitura

#Escrita de arquivos
"""
    Para escrever dados em um arquivo, abrimos em modo de escrita ("w") utilizando a função open(). Se o arquivo não existir, será criado automaticamente. Se o arquivo já existir, seu conteúdo será sobrescrito.
"""
arquivo = open("dados.txt", "w")
arquivo.write("Olá, mundo!")
arquivo.close()  # Fechando o arquivo após a escrita

"""
    Neste exemplo, o arquivo "dados.txt" é aberto em modo de escrita utilizando open(). Depois, a string "Olá, mundo!" é escrita no arquivo utilizando o método write(). Finalmente, o arquivo é fechado utilizando o método close().
"""

"""
    Importante: sempre fechar o arquivo após a leitura ou escrita é uma boa prática para evitar problemas de acesso e garantir que os recursos do sistema sejam liberados corretamente.
    Além disso, podemos utilizar o gerenciador de contexto with para abrir arquivos, que garante que o arquivo seja fechado automaticamente após o bloco de código ser executado, mesmo que ocorra uma exceção.
    Exemplo:
    with open("exemplo.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
    Neste exemplo, o arquivo "exemplo.txt" é aberto em modo de leitura utilizando open() dentro de um bloco with. O arquivo será fechado automaticamente ao final do bloco, mesmo que oc
"""