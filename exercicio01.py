import math
def produtoNumeros():
    num1 = input("Digite um numero inteiro: ")
    num2 = input("Digite um numero inteiro: ")
    num3 = input("Digite um numero real: ").replace(",",".")

    if isinstance(num1,int) != True or isinstance(num2, int) != True:
        print("os dois numeros iniciais precisam ser inteiros, inicie novemente o programa")
        return
    
    if isinstance(num3, float) != True:
        print("os tericeiro numeros precisam ser real, inicie novemente o programa")
        return

    produtoA = (num1 * 2) + (num2 / 2)
    produtoB = (num1 * 3) + num3
    produtoC = math.pow(num3, 3)

    print(f"O produto do dobro do primeiro com metade do segundo:  {produtoA:.2f}")
    print(f"A soma do triplo do primeiro com o terceiro:  {produtoB:.2f}")
    print(f"O terceiro número elevado ao cubo.  {produtoC:.2f}")
produtoNumeros() 

