"""
Escreva a função maior_elemento que recebe como parâmetro uma lista
com números inteiros e devolve um número inteiro correspondente ao maior
valor presente na lista recebida.
"""

lista = [7,3,33,12,3,3,3,7,12,100]

def maior_elemento(lista):

    lista.sort()

    print(lista)
    print(lista[-1])
    
    return lista[-1]

maior_elemento(lista)
