"""

Escreva a função maior_primo que recebe um número inteiro maior ou
igual a 2 como parâmetro e devolve o maior número primo menor ou igual
ao número passado à função

***Eu quase morro nesse exercício***

"""

def éprimo(k):
        divisor = 1
        dividiu = 0
        primo = 0
        while divisor <= k:
                if k % divisor == 0:
                        dividiu = dividiu + 1
                divisor = divisor + 1
        if dividiu == 2:
                primo = k
                return(True)
        else:
                return(False)
        

def maior_primo(n):
        testanumero = 2
        primo = 0
        while testanumero < n:
                éprimo(testanumero)
                testanumero = testanumero + 1
                if éprimo(testanumero) == True:
                        primo = testanumero
        return primo
        
        

                                
        
                
        
