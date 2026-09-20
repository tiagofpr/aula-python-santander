# 3 Estrutura de controle

# Estrutura condicional if, elif e else

# if condicao:
#     # bloco de código executado se a condição for verdadeira
#     instrucoes

#exemplo
idade = 18

if idade >= 18:
    print("Você é maior de idade.")

#if-else
idade = 16

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

#if-elif-else
idade = 20 
if idade < 18:
    print("Você é menor de idade.")
elif idade >= 18 and idade < 65:
    print("Você é adulto.")
else:
    print("Você é idoso.")

