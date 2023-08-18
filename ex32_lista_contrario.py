"""
Dados n > 0 e uma sequência com n números reais, imprimí-los na ordem inversa
a da leitura.
"""

def main():

    n = int(input("Digite a quantidade de elementos na lista: "))

    lista = []
    quantos = 0

    while quantos < n:
        elemento = int(input("Digite um elemento: "))
        lista.append(elemento)
        quantos += 1
        
    print("A lista contém os seguintes elementos: ",lista)

    rev = 0
    for i in lista:
        rev -= 1
        print(lista[rev])

main()

    
