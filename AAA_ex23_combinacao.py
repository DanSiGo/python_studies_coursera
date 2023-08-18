"""

Usando a função do exercício 6.2, escreva uma função que recebe dois inteiros, m e n, como parâmetros e retorna a combinação m!/((m-n)!n!).


def combinacao(m, n):
    '''(int, int) -> int
    Recebe dois inteiros m e n, e retorna o valor de m!/((m-n)! n!)
    '''
 
    # COMPLETE ESSA FUNÇÃO E MUDE O RETURN ABAIXO
 
    return "o resultado"
 
# testes
print("Combinacao(4,2) =", combinacao(4,2))
print("Combinacao(5,2) =", combinacao(5,2))
print("Combinacao(10,4) =", combinacao(10,4))

"""

def combinacao(m,n):

    resultado = fatorial(m)/(fatorial(m-n) * fatorial(n))

    return int(resultado)

def fatorial(k):

    k_fat = 1
    n = 1

    while n <= k:
        k_fat = k_fat * n
        n = n + 1

    return k_fat

print("Combinacao(4,2) =", combinacao(4,2))
print("Combinacao(5,2) =", combinacao(5,2))
print("Combinacao(10,4) =", combinacao(10,4))
