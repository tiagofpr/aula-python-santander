# 6.1 Tratamento de exceções em Python

# try

"""
o bloco try é usado para envolver o código que pode gerar uma exceção.
Se uma exceção ocorrer dentro do bloco try, o fluxo de execução será interrompido e o controle será transferido para o bloco except correspondente.
Se nenhuma exceção ocorrer, o bloco except será ignorado e o programa continuará a execução normalmente.
"""
try:
    #código que pode gerar uma exceção
    resultado = 10 / 0
    print("O resultado é:", resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")

#Except
"""
O bloco except é usado para capturar e tratar exceções específicas que podem ocorrer dentro do bloco try. 
Podemos ter múltiplos blocos except para tratar diferentes tipos de exceções.
"""

try:
    #código que pode gerar uma exceção
    resulado = 10 /0 #divisão por zero
    print("O resultado é:", resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
except ValueError:
    print("Erro: Valor inválido.")

#Finally
"""
O bloco finally é usado para definir um conjunto de instruções que serão executadas independentemente de uma exceção ter ocorrido ou não.
"""

try:
    #código que pode gerar uma exceção
    arquivo = open("arquivo.txt", "r")
    #realizar operações com o arquivo
except FileNotFoundError:
    print("Erro: Arquivo não encontrado.")
finally:
    arquivo.close()  # O arquivo será fechado independentemente de uma exceção ter ocorrido ou não.


#6.2 Exceções personalizadas

"""
Além das exceções incorporadas no Python, você também pode criar suas próprias exceções personalizadas. 
Isso é útil quando deseja lidar com situações específicas do seu programa.
Para criar uma exceção personalizada, você deve criar uma classe que herde da classe base Exception ou de uma de suas subclasses.
"""
# def  funcao():
#     #Código que pode gerar uma exceção personalizada
#     if condicao:
#         raise Exception("Mensagem de erro personalizada")

# try:
#     funcao()
# except Exception as e:
#     print(f"Ocorreu uma exceção: {str(e)}")

"""
    Neste exemplo, a função funcao() verifica uma condição e, se for verdadeira, lança uma exceção personalizada com uma mensagem de erro. 
    O bloco try-except captura a exceção e exibe a mensagem correspondente.
"""

def funcao():
    # Código que pode gerar uma exceção personalizada
    condicao = True  # Exemplo de condição
    if condicao:
        raise Exception("Mensagem de erro personalizada")
try:
    funcao()
except Exception as e:
    print(f"Ocorreu uma exceção: {str(e)}")