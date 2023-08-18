"""
Escreva a função n_primos que recebe como argumento um número inteiro maior
ou igual a 2 como parâmetro e devolve a quantidade de números primos que
existem entre 2 e n (incluindo 2 e, se for o caso, n).
"""

def n_primos(n):
    contador = 0
    numero = 1
    primos = []
    while numero < n:
        i = 1
        numero = numero + 1
        while i < numero:
            i = i + 1
            if numero % i == 0 and numero != 2:                
                break
           
            elif (numero % i != 0 and i == (numero-1)) or numero == 2:                
                contador = contador + 1
                primos.append(numero)
            
    print(contador)
    print(primos)
    return(contador)
    
n_primos(100)

  
