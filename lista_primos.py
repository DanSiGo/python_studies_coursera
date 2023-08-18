n = int(input("Limite máximo: "))
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
            
print("Essa lista contém %d número primos" %contador)
print("Elementos dentro da lista primos:", primos)

