def calcular_coeficientes_expansao(n):
    coeficientes = [1]  # O primeiro coeficiente é sempre 1

    for i in range(1, n + 1):
        novo_coeficiente = coeficientes[-1] * (n - i + 1) // i
        coeficientes.append(novo_coeficiente)

    return coeficientes

n = int(input("Digite um valor inteiro não negativo: "))
coeficientes = calcular_coeficientes_expansao(n)

print("Coeficientes da expansão de (x+y)^{}:".format(n))
for coeficiente in coeficientes:
    print(coeficiente, end=" ")
