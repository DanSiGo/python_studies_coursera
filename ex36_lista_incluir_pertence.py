def pertence(item, lista):
    
    if item in lista:
        print("O item",item, "já está na lista")
    else:
        print("O item", item, "não está na lista e será adicionado")
        return lista.append(item)

n = int(input("Digite o nº de elementos da lista: "))
conta_elementos = 0
lista = []

while conta_elementos < n:
    elementos = int(input("Digite os elemento da lista: "))
    pertence(elementos, lista)
    print("A lista contém: ", lista)
    conta_elementos += 1

print(lista)
