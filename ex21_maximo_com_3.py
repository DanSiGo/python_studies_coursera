"""

Reescreva a função 'maximo' do outro exercício, que devolve o
maior valor dentre dois inteiros recebidos, para que ela passe a
receber 3 valores inteiros como parâmetros e devolva o maior dentre eles.

"""

def maximo(a, b, c):
    if (a >= b) and (a >= c):
        return a

    if (b >= a) and (b >= c):
        return b

    if (c >= a) and (c >= b):
        return c

    
