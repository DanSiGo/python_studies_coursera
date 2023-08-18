"""
programa que leia sequencia de numero inteiros terminadas por 0
quando usuario digita o 0, imprime a lista na ordem inversa
"""

i = 0
lis = []


print("Digite uma sequência de números. Digite 0 para finalizar")
while i < 1:
    numero = (int(input("Digite o número: ")))    
    if numero == 0:
        i = len(lis)
    else:
        lis.append(numero)

tam = len(lis) - 1

if numero == 0:
    while tam >= 0:
        print(lis[tam], end = ", ")
        tam = tam - 1
        
