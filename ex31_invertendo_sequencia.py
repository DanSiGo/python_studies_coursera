"""
Como pedido na primeira video-aula desta semana, escreva um programa que
recebe uma sequência de números inteiros e imprima todos os valores em ordem
inversa. A sequência sempre termina pelo número 0. Note que 0 (ZERO) não deve
fazer parte da sequência.
"""
# essa solução faz coloca a lista em ordem invertida
"""

lista = []

elemento = 1

while elemento > 0:
    elemento = int(input("Digite um nº, ou 0 para encerrar: "))
    
    if elemento != 0:
        lista.append(elemento)
        

lista.sort(reverse=True)

print(lista[0],"\n",lista[1],"\n",lista[2], sep="")

"""    
# mas o exercício quer que inverta a ordem em que foram inseridos os elementos

lista = []

elemento = 1

while elemento > 0:
    elemento = int(input("Digite um nº, ou 0 para encerrar: "))
    
    if elemento != 0:
        lista.append(elemento)

inver = 0
for i in lista:
    inver = inver - 1
    print(lista[inver])







