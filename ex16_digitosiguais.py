n = int(input("Digite um número inteiro: "))

sim = 0
nao = 0

while n > 0:
        dig1 = n % 10
        n = n // 10
        dig2 = n % 10
        
        if dig1 == dig2:
                sim = sim + 1
        elif dig1 != dig2 and n <= 0:
                nao = nao + 1

if sim > 0:
        print("sim")
else:
        print("não")
                


