def indice(item, lista):
    '''(objeto,list) -> int ou None

    Recebe um objeto 'item' e uma lista 'lista' e retorna o
    indice da posicao em que item ocorre na lista.
    Caso item nao ocorra na lista a funcao retorna None
    '''
    
    if item in lista:
        indice = lista.index(item)
        print("O elemento está na posição:", indice)
    else:
        print("O item não está na lista")
        return None



lista = [1, "oi", 3.14, 7, True]

indice(False, lista)

  
