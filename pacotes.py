#8.2 Pacotes

"""
    Pacotes são uma forma de organizar módulos em diretórios, permitindo uma estrutura hierárquica para o código. 
    Um pacote é um diretório que contém um arquivo especial chamado __init__.py, que indica que o diretório deve ser tratado como um pacote.
    Podemos ter pacotes dentro de pacotes, criando uma estrutura de diretórios aninhada.
"""

# meu_pacote/
#     __init__.py  # Arquivo que indica que este diretório é um pacote
#     modulo1.py  # Módulo 1 do pacote
#     modulo2.py  # Módulo 2 do pacote

from meu_pacote import modulo1, modulo2  # Importando os módulos do pacote meu_pacote

modulo1.funcao1()  # Chamando a função do módulo 1
modulo2.funcao2()  # Chamando a função do módulo 2
