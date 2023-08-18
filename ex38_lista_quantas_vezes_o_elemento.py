#-----------------------------------------------
def main():
    '''
    Dados n e uma sequencia com n numeros inteiros,
    conta e imprime o numero de vezes que cada
    numero ocorre na sequencia.
    '''

    n = int(input("Digite a quantidade de elementos na lista: "))

    lista = []
    quantos = 0

    while quantos < n:
        elemento = int(input("Digite um elemento: "))
        lista.append(elemento)
        quantos += 1
        
    print("A lista contém os seguintes elementos: ",lista)

    lista2 = []

    for i in lista:
        if i not in lista2:
            lista2.append(i)    
    
    for i in lista2:        
        print("O número %d ocorre %d vezes na lista" % (i, lista.count(i)))


main()
