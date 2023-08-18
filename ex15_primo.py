n = int(input("Digite um número inteiro: "))

dividepor = 0
numeroadiv = 0

while numeroadiv < n:
        numeroadiv += 1
        if n % numeroadiv == 0:
                dividepor += 1

if dividepor > 2:
        print("não primo")

else:
        print("primo")

