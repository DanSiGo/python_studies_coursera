"""
Dada uma sequência de n > 0 números reais, imprimi-los eliminando as repetições.
"""

lista = [7,3,33,12,3,3,3,7,12,100]

def main():
    print ("The original list is : "+ str(lista))
     
    res = []
    for i in lista:
        if i not in res:
            res.append(i)

    print ("The list after removing duplicates : "+ str(res))

main()

    
# resposta do GEEKS FOR GEEKS

#   nessa solução ele cria uma segunda lista que vai adicionando elementos
#   a medida em que o for vai passando pelos elementos da lista inicial, e inclui um
# if not in para adicionar o elemento em que o for está passando caso esse elemento
# nao conste na segunda lista, genial

# utiliza o >>> if not in res: <<<
