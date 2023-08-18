"""
Dados dois números naturais m e n e duas sequências ordenadas com m e n números
inteiros, obter uma única sequência ordenada contendo todos os elementos das
sequências originais sem repetição.

Sugestão: Imagine uma situação real, por exemplo, dois fichários de uma
biblioteca.

------------------- NO FINAL - EXPLICAÇÃO DE SORT OU SORTED--------------------


"""

m = int(input("Digite o nº de elementos da lista 1: "))
n = int(input("Digite o nº de elementos da lista 2: "))

conta_elementos = 0

lista1 = []
lista2 = []

lista_final = []

while conta_elementos < m:
    elementos = int(input("Digite os elemento da lista 1: "))
    lista1.append(elementos)
    conta_elementos += 1

conta_elementos = 0

while conta_elementos < n:
    elementos = int(input("Digite os elemento da lista 2: "))
    lista2.append(elementos)
    conta_elementos += 1

print("A lista 1 contém: ", lista1)
print("A lista 2 contém: ", lista2)

for i in lista1:
    if i not in lista_final:
        lista_final.append(i)

for i in lista2:
    if i not in lista_final:
        lista_final.append(i)

print("Lista final, contendo elementos não repetidos das duas listas: ", lista_final)

# SORT OU SORTED?

print("Lista final em ordem crescente com SORTED: ", sorted(lista_final))
print("Lista final depois do SORTED: ", lista_final)
lista_final.sort()
print("Lista final em ordem crescente com SORT: ", lista_final)
print("SORT altera a lista, por isso deve ser utilizado fora do print e no print só imprime a lista")

