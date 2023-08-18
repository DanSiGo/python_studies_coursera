""" 
Escreva a função remove_repetidos que recebe como parâmetro uma 
lista com números inteiros, verifica se tal lista possui 
elementos repetidos e os remove. A função deve devolver uma lista 
correspondente à primeira lista, sem elementos repetidos. A lista 
devolvida deve estar ordenada.

Dica: Você pode usar lista.sort() ou sorted(lista). Qual a 
diferença? 

"""

lista = [7,3,33,12,3,3,3,7,12,100]

def remove_repetidos(lista):
    lista_r = lista[:]
    numero = 0
    
    for i in lista_r:
        contador = 0
        numero = i      # guardar um elemento da lista      
        
        for x in lista_r:     # passar novamente pela lista            
            if x == numero:     # se o elemento guardado estiver na lista
                contador = contador + 1
                if contador > 1:
                    lista_r.remove(numero)

    for i in lista_r:
        contador = 0
        numero = i      # guardar um elemento da lista      
        
        for x in lista_r:     # passar novamente pela lista            
            if x == numero:     # se o elemento guardado estiver na lista
                contador = contador + 1
                if contador > 1:
                    lista_r.remove(numero)
                    

    lista_r.sort()
    print(lista_r)
    return lista_r

remove_repetidos(lista)
                    
                    





