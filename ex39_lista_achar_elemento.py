'''(objeto,list) -> int ou None

    Recebe um objeto 'item' e uma lista 'lista' e retorna o
    indice da posicao em que item ocorre na lista.
    Caso item nao ocorra na lista a funcao retorna None
'''
lista  = [1, 2, 3, 4, 5]

def indice(item, lista):

    seq = lista

    indice = lista.index(item)

    return indice


indice(3, lista)