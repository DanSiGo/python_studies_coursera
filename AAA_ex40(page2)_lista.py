"""
    Dados n e uma sequencia com n numeros inteiros,
    conta e imprime o numero de vezes que cada
    numero ocorre na sequencia.
"""

lista  = [1, 1, 2, 2, 3, 4, 5, 29, 10, 9, 2, 32, 43, 43, 2, 1, 10]

def main():
    lista2 = []
    for i in lista:
        if i not in lista2:
            lista2.append(i)
    lista2.sort()

    for i in lista2:
        indice(i, lista)


def indice(item, lista):
    cont = 0
    indice = lista.index(item)
    
    for i in  lista:
        if i == item:
            cont += 1
    print(f"O item {item} aparece {cont} vezes na lista")
    return None

main()


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Como fazer utilizando a função indice???????????????????