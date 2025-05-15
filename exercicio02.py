def maiorNumero():
    try:
        num1 = float(input("Digite o 1° numero natural: "))
        num2 = float(input("Digite o 2° numero natural: "))

        if isinstance(num1, (float , int)) != True or isinstance(num2, (float, int)) != True  :
            print("O valor digitado não é um numero real")
            return
        else:
            maior = max(num1, num2)
            print(f"o maior numero é: {maior:.1f}")
    except ValueError:
        print("Valor inserido invalido, tentar novamente")
maiorNumero()