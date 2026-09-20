#3.1 Loops

#for
# for variavel_in_sequencia:
#     #bloco de codigo a repetir
#     instrucoes

#exemplo
frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    print(fruta)
# Neste exemplo, o loop for percorre cada elemento da lista frutas e imprime o nome de cada fruta.

print("Numeros de 1 a 5 multiplicados por 2:")
for numero in range(1, 6):
    print(numero * 2)

# while
# o loop while executa um bloco de código enquanto uma condição for verdadeira.
# while condicao:
#     #bloco de codigo a repetir
#     instrucoes

#exemplo
contador = 0
while contador < 5:
    print(contador)
    contador +=1
# neste exemplo, o loop while imprime os números de 0 a 4, incrementando o valor do contador a cada iteração até que a condição contador < 5 seja falsa.

print("Numeros de 1 a 5 multiplicados por 2:")
contador = 1
while contador <= 5:
    print(contador * 2)
    contador += 1

#Controlando o loop com break e continue
# O comando break é usado para sair de um loop antes que ele termine normalmente.
# O comando continue é usado para pular a iteração atual e continuar com a próxima iteração do loop.

print("Exemplo de break:")
contador = 0 

while True:
    print(contador)
    contador += 1

    if contador == 5:
        break

print("Exemplo de continue:")
for i in range(10):
    if i % 2 ==0:
        continue
    print(i)
#neste exemplo, o loop for percorre os números de 0 a 9 e, quando encontra um número par (i % 2 == 0),
# o comando continue é acionado, pulando a iteração atual e continuando com a próxima iteração do loop.

#Pass
#A instrução pass é usada como um marcador de posição em blocos de código que ainda não foram implementados.
# Ela não faz nada e é útil quando você precisa de um bloco de código vazio, mas não quer que o interpretador Python gere um erro de sintaxe.
print("Exemplo de pass:")
for i in range(5):
    pass  # Este loop não faz nada, mas é sintaticamente válido.