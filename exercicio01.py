import math
def produtoNumeros():
    num1 = int(input("Digite um numero inteiro: "))
    num2 = int(input("Digite um numero inteiro: "))
    num3 = float(input("Digite um numero real: ").replace(",","."))

    produtoA = (num1 * 2) + (num2 / 2)
    produtoB = (num1 * 3) + num3
    produtoC = math.pow(num3, 3)

    print(f"O produto do dobro do primeiro com metade do segundo:  {produtoA:.2f}")
    print(f"A soma do triplo do primeiro com o terceiro:  {produtoB:.2f}")
    print(f"O terceiro número elevado ao cubo.  {produtoC:.2f}")
produtoNumeros() 

