largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

i = 0


while i < altura:
    i = i+1
    if i == 1 or i == altura:
        print(largura * "#")
    else:
        print("#", end = "")
        print((largura - 2) * " ", end = "")
        print("#")
    
